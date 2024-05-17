from qtpy.QtWidgets import QLabel, QFileDialog
from qtpy.QtGui import QPixmap, QColor, QPainter, QImageWriter, QPolygonF, QPainterPath, QPen, QBrush
from qtpy.QtCore import Qt, QRect, QEvent, Signal, QByteArray, QPoint, QLineF, QPointF
from datetime import datetime

import math
import json
import shutil
from pathlib import Path

class Canvas(QLabel):

    # Define a signal to emit the drawn shape
    shapeAdded = Signal(str, QColor, str, list)

    def __init__(self):
        super().__init__(parent=None)
        self.pixmap = QPixmap(self.size())
        self.pixmap.fill(Qt.white)
        self.setPixmap(self.pixmap)

        self.start_x, self.start_y = None, None
        self.end_x, self.end_y = None, None
        self.image_path = None
        self.current_label = None
        self.project_folder = None
        self.pen_color = QColor('#000000')

        self.draw_shape = "rectangle"  # Variable to store the shape to be drawn
        self.shapes = []

        self.zoom_factor = 1.0

        # Initialize polyline points list
        self.polyline_points = []

        # Initialize Bezier curve control points list
        self.bezier_control_points = []

        # Initialize polygon points list
        self.polygon_points = []
    
    def setProjectFolder(self, folder):
        self.project_folder = folder

    def setLabel(self, label):
        self.current_label = label
        self.setDrawShape(self.draw_shape)

    def setBackgroundImage(self, image_path):
        self.clear()
        self.shapes = []
        self.pixmap = QPixmap(image_path)
        self.setPixmap(self.pixmap)
        self.image_path = image_path

        self.setDrawShape(self.draw_shape)

        # load shapes if available
        self.loadImageAnnotations(self.image_path)
    
    def saveData(self):
        if not self.project_folder or not self.image_path or not self.current_label:
            return False

        # Move the image to the "images" directory if it doesn't exist there already
        image_filename = Path(self.image_path).name
        images_folder = Path(self.project_folder) / "images"
        
        if not images_folder.exists():
            images_folder.mkdir(parents=True)  # Create the "images" folder if it doesn't exist
        if not (images_folder / image_filename).exists():
            shutil.copy(self.image_path, images_folder)

        # Create a dictionary to store the annotation data
        annotation_data = {
            "image_path": str(Path("images") / image_filename),
            "annotations": []
        }

        # Create a dictionary to group shapes by label
        label_to_shapes = {}

        # Iterate over the shapes and extract their information
        for shape, color, label, coords in self.shapes:
            # Convert QPointF or QPoint objects to tuples
            coords = [coord.toTuple() if isinstance(coord, (QPointF, QPoint)) else coord for coord in coords]
            # Depending on the shape type, you might need to extract different information
            shape_data = {
                "type": shape,
                "color": color.name(),
                "coordinates": coords
            }
            
            # Group shapes by label
            if label not in label_to_shapes:
                label_to_shapes[label] = []
            label_to_shapes[label].append(shape_data)

        # Create annotations for each label
        for label, shapes in label_to_shapes.items():
            annotation_data["annotations"].append({
                "label": label,
                "shapes": shapes
            })

        # Write the annotation data to a JSON file
        annotation_filename = image_filename + ".json"
        annotation_filepath = Path(self.project_folder) / annotation_filename
        try:
            with open(annotation_filepath, "w") as f:
                json.dump(annotation_data, f, indent=4)
        except Exception as e:
            # print(annotation_data)
            print(e)
        

        return True

    def loadImageAnnotations(self, image_url):
        # Construct the path to the JSON file corresponding to the image URL
        image_filename = Path(image_url).name
        annotation_filename = image_filename + ".json"
        json_file_path = Path(self.project_folder) / annotation_filename

        # Read the annotation data from the JSON file
        if json_file_path.exists():
            with open(json_file_path, 'r') as f:
                annotation_data = json.load(f)
            
            # Clear existing shapes
            self.shapes = []

            # Update self.shapes with annotation data
            annotations = annotation_data.get('annotations', [])
            for annotation in annotations:
                label = annotation.get('label')
                shapes = annotation.get('shapes', [])
                for shape_data in shapes:
                    shape_type = shape_data.get('type')
                    color = QColor(shape_data.get('color'))
                    coordinates = shape_data.get('coordinates')

                    # Convert coordinates to QPointF if the shape is polyline or bezier
                    if shape_type in ['polyline', 'bezier', 'polygon']:
                        coordinates = [QPointF(coord[0], coord[1]) if isinstance(coord, list) else QPointF(coord.x(), coord.y()) for coord in coordinates]

                    self.shapeAdded.emit(shape_type, color, label, coordinates)
                    self.shapes.append((shape_type, color, label, coordinates))

            # Update canvas to reflect the changes
            self.updateCanvas()
    
    def deleteShapeFromJson(self, image_url, shape_to_delete):
        # Construct the path to the JSON file corresponding to the image URL
        image_filename = Path(image_url).name
        annotation_filename = image_filename + ".json"
        json_file_path = Path(self.project_folder) / annotation_filename

        # Check if the JSON file exists
        if not json_file_path.exists():
            return False  # JSON file doesn't exist, unable to delete shape

        # Convert QColor to a format compatible with your data
        shape_to_delete_converted = (
            shape_to_delete[0], 
            shape_to_delete[1].name(),  # Convert QColor to hexadecimal color string
            shape_to_delete[2], 
            shape_to_delete[3]
        )
        new_shape = {
            "type": shape_to_delete[0],
            "color": shape_to_delete[1],
            "coordinates": shape_to_delete[3]
        }
        
        # Load existing annotation data from the JSON file
        with open(json_file_path, "r") as f:
            annotation_data = json.load(f)
        
        # Iterate over annotations and remove the specified shape
        for annotation in annotation_data["annotations"]:
            shapes = annotation["shapes"]
            # Filter out the shape to delete based on type, color, and coordinates
            annotation["shapes"] = []
            for shape in shapes:
                if shape != new_shape:
                    annotation["shapes"].append(shape)

        # Write the modified annotation data back to the JSON file
        with open(json_file_path, "w") as f:
            json.dump(annotation_data, f, indent=4)

        return True  # Shape deletion successful

    def readLabelsFromJsonFiles(self):
        labels = set()  # Using a set to store unique labels
        
        # Iterate over all files in the directory
        for json_file_path in Path(self.project_folder).glob("*.json"):
            # Open the JSON file and read its contents
            try:
                with open(json_file_path, 'r') as f:
                    data = json.load(f)
            except:
                pass
            
            # Iterate over annotations and extract labels
            for annotation in data.get('annotations', []):
                label = annotation.get('label')
                if label:
                    labels.add(label)
        
        return labels

    def setPenColor(self, c):
        self.pen_color = QColor(c)

    def setDrawShape(self, shape):
        if shape == "polyline":
            # Clear previous points when switching to polyline mode
            self.polyline_points = []
        elif shape == "bezier":
            # Clear previous control points when switching to Bezier mode
            self.bezier_control_points = []
        elif shape == "polygon":
            # Clear previous control points when switching to Bezier mode
            self.polygon_points = []

        self.draw_shape = shape

    def adjustSizeToContent(self):
        size = self.parent().size()
        self.adjustSize()

    def eventFilter(self, obj, e: QEvent):
        # if self.parent() and obj is self.parent().window():
        if e.type() in [QEvent.Resize, QEvent.Paint]:
            self.adjustSizeToContent()

        return super().eventFilter(obj, e)

    def showEvent(self, e):
        super().showEvent(e)
        if self.parent():
            self.parent().installEventFilter(self)
        self.adjustSizeToContent()

    def mousePressEvent(self, e):
        if self.draw_shape == "polyline" and e.buttons() == Qt.LeftButton:
            # Add the start point of the polyline
            self.polyline_points.append(e.position())
            self.updateCanvas(update=True)
        elif self.draw_shape == "polyline" and e.buttons() == Qt.RightButton:
            # self.polyline_points.append(e.position())
            self.updateCanvas()
            self.shapeAdded.emit(self.draw_shape, self.pen_color, self.current_label, self.polyline_points)
            self.shapes.append((self.draw_shape, self.pen_color, self.current_label, self.polyline_points))
            # Clear previous points when switching to polyline mode
            self.polyline_points = []
        elif self.draw_shape == "bezier" and e.buttons() == Qt.LeftButton:
            # Add the control point of the Bezier curve
            self.bezier_control_points.append(e.position())
            self.updateCanvas()
        elif self.draw_shape == "bezier" and e.buttons() == Qt.RightButton:
            # self.polyline_points.append(e.position())
            self.updateCanvas()
            self.shapeAdded.emit(self.draw_shape, self.pen_color, self.current_label, self.bezier_control_points)
            self.shapes.append((self.draw_shape, self.pen_color, self.current_label, self.bezier_control_points))
            # Clear previous points when switching to polyline mode
            self.bezier_control_points = []
        
        elif self.draw_shape == "polygon" and e.buttons() == Qt.LeftButton:
            # Add the control point of the Bezier curve
            self.polygon_points.append(e.position())
            self.updateCanvas()
        elif self.draw_shape == "polygon" and e.buttons() == Qt.RightButton:
            # self.polyline_points.append(e.position())
            self.updateCanvas()
            self.shapeAdded.emit(self.draw_shape, self.pen_color, self.current_label, self.polygon_points)
            self.shapes.append((self.draw_shape, self.pen_color, self.current_label, self.polygon_points))
            # Clear previous points when switching to polyline mode
            self.polygon_points = []

        else:
            self.start_x = e.position().x()
            self.start_y = e.position().y()

    def mouseMoveEvent(self, e):
        if self.draw_shape == "polyline" and e.buttons() == Qt.LeftButton:
            # Add intermediate points of the polyline
            self.polyline_points.append(e.position())
            self.updateCanvas(update=True)
        elif self.draw_shape == "bezier" and e.buttons() == Qt.LeftButton:
            # Update the last control point of the Bezier curve
            if self.bezier_control_points:
                self.bezier_control_points[-1] = e.position()
                self.updateCanvas(update=True)
        elif self.draw_shape == "polygon" and e.buttons() == Qt.LeftButton:
            # Update the last control point of the Bezier curve
            if self.polygon_points:
                self.polygon_points[-1] = e.position()
                self.updateCanvas(update=True)

        elif e.buttons() & Qt.LeftButton:
            self.end_x = e.position().x()
            self.end_y = e.position().y()
            # Update the end point of the shape
            update = True
            if self.start_x and self.start_y:
                self.updateCanvas(update=update)

    def mouseReleaseEvent(self, e):
        if self.draw_shape == "polyline":
            # Add intermediate points of the polyline
            self.polyline_points.append(e.position())
            # Update canvas to show the preview of the polyline
            self.updateCanvas(update=True)
        elif self.draw_shape == "bezier":
            # Add control points for Bezier curves
            self.bezier_control_points.append(e.position())
            self.updateCanvas(update=True)
        
        elif self.draw_shape == "polygon":
            # Add control points for Bezier curves
            self.polygon_points.append(e.position())
            self.updateCanvas(update=True)

        elif e.button() == Qt.LeftButton:
            self.end_x = e.position().x()
            self.end_y = e.position().y()
            # Save the drawn shape and its bounding rectangle
            self.shapes.append((self.draw_shape, self.pen_color,  self.current_label, [self.start_x, self.start_y, self.end_x, self.end_y]))
            # Emit the shapeAdded signal with shape information
            self.shapeAdded.emit(self.draw_shape, self.pen_color, self.current_label, [self.start_x, self.start_y, self.end_x, self.end_y])
            self.updateCanvas()

    def updateCanvas(self, update=False):
        if not self.image_path:
            return
        
        # Clear the canvas and redraw all shapes
        self.pixmap = QPixmap(self.image_path)
        self.setPixmap(self.pixmap)
        painter = QPainter(self.pixmap)

        # Draw the background image
        painter.drawPixmap(0, 0, self.pixmap)

        for shape, color, label, coords in self.shapes:
            p = painter.pen()
            p.setWidth(3)
            p.setColor(color)
            painter.setPen(p)
            painter.setBrush(Qt.NoBrush)
            if shape == "line":
                start_x, start_y, end_x, end_y = coords
                painter.drawLine(start_x, start_y, end_x, end_y)
            elif shape == "rectangle":
                start_x, start_y, end_x, end_y = coords
                rect = QRect(start_x, start_y, end_x - start_x, end_y - start_y)
                painter.drawRect(rect)
            elif shape == "ellipse":
                start_x, start_y, end_x, end_y = coords
                rect = QRect(start_x, start_y, end_x - start_x, end_y - start_y)
                painter.drawEllipse(rect)
            elif shape == "polyline":
                # Draw polyline
                if coords is not None:
                    valid_coords = [point for point in coords if point is not None]
                    try:
                        points = [QPoint(point.x(), point.y()) for point in valid_coords]  # Convert QPointF to QPoint
                        if len(points) > 1:
                            painter.drawPolyline(QPolygonF(points))
                    except Exception as e:
                        print("Coords:", coords, " - ", e)

            elif shape == "bezier":
                valid_coords = [point for point in coords if point is not None]
                points = [QPoint(point.x(), point.y()) for point in valid_coords]  # Convert QPointF to QPoint
                if len(points) > 1:
                    self.doBezierCurveDrawing(painter, points)

            elif shape == "polygon":
                valid_coords = [point for point in coords if point is not None]
                points = [QPoint(point.x(), point.y()) for point in valid_coords]  # Convert QPointF to QPoint
                if len(points) > 2:
                    # Create a QPolygonF object from the points
                    polygon = QPolygonF(points)

                    # Draw the polygon
                    painter.drawPolygon(polygon)

        if update:
            p = painter.pen()
            p.setWidth(2)
            p.setColor(self.pen_color)
            painter.setPen(p)
            if self.draw_shape == "line":
                painter.drawLine(self.start_x, self.start_y, self.end_x, self.end_y)
            elif self.draw_shape == "rectangle":
                rect = QRect(self.start_x, self.start_y, self.end_x - self.start_x, self.end_y - self.start_y)
                painter.drawRect(rect)
            elif self.draw_shape == "ellipse":
                rect = QRect(self.start_x, self.start_y, self.end_x - self.start_x, self.end_y - self.start_y)
                painter.drawEllipse(rect)
            elif self.draw_shape == "polyline":
                # Draw polyline
                if self.polyline_points and len(self.polyline_points) > 1:
                    points = [QPoint(point.x(), point.y()) for point in self.polyline_points]  # Convert QPointF to QPoint
                    painter.drawPolyline(points)
            elif self.draw_shape == "bezier":
                self.doBezierCurveDrawing(painter, self.bezier_control_points)
            
            elif self.draw_shape == "polygon":
                # Draw polygon
                if self.polygon_points and len(self.polygon_points) > 2:
                    points = [QPoint(point.x(), point.y()) for point in self.polygon_points]  # Convert QPointF to QPoint
                    # Create a QPolygonF object from the points
                    polygon = QPolygonF(points)
                    # Draw the polygon
                    painter.drawPolygon(polygon)

        else:
            self.start_x, self.start_y, self.end_x, self.end_y = None, None, None, None
        
        painter.end()
        self.setPixmap(self.pixmap)

    def doBezierCurveDrawing(self, painter: QPainter, controlPoints):

        redPen = QPen(Qt.red, 2)
        bluePen = QPen(Qt.blue, 2)
        redBrush = QBrush(Qt.red)
        blackPen = QPen(Qt.black, 2)

        steps = 1000
        oldPoint = controlPoints[0]

        painter.setBrush(redBrush)
        painter.drawEllipse(oldPoint.x() - 3, oldPoint.y() - 3, 6, 6)

        painter.drawText(oldPoint.x() + 5, oldPoint.y() - 3, '1')
        for i, point in enumerate(controlPoints[1:]):
            i += 2
            painter.setPen(redPen)
            painter.drawLine(oldPoint.x(), oldPoint.y(), point.x(), point.y())
            
            painter.setPen(redPen)
            painter.drawEllipse(point.x() - 3, point.y() - 3, 6, 6)

            painter.drawText(point.x() + 5, point.y() - 3, '%d' % i)
            oldPoint = point
 
        painter.setPen(bluePen)
        for point in self.bezierCurveRange(steps, controlPoints):
            painter.setPen(blackPen)
            try:
                painter.drawLine(oldPoint[0], oldPoint[1], point[0], point[1])
            except Exception as e:
                pass
                try:
                    painter.drawLine(oldPoint.x(), oldPoint.y(), point[0], point[1])
                except Exception as e:
                    pass
            oldPoint = point

    
    def bezierCurveRange(self, n, points):
        """Range of points in a curve bezier"""
        for i in range(n):
            t = i / float(n - 1)
            yield self.bezier(t, points)
    
    def binomial(self, i, n):
        """Binomial coefficient"""
        return math.factorial(n) / float(
            math.factorial(i) * math.factorial(n - i))


    def bernstein(self, t, i, n):
        """Bernstein polynom"""
        return self.binomial(i, n) * (t ** i) * ((1 - t) ** (n - i))


    def bezier(self, t, points):
        """Calculate coordinate of a point in the bezier curve"""
        n = len(points) - 1
        x = y = 0
        for i, pos in enumerate(points):
            bern = self.bernstein(t, i, n)
            x += pos.x() * bern
            y += pos.y() * bern
        return x, y

    def deleteShape(self, shape):
        # Iterate through the list of shapes and remove the specified shape
        for s in self.shapes:
            if s == shape:
                self.shapes.remove(s)
                break
            # else:
            #     print("shape not found")
            #     print(self.shapes)
        self.deleteShapeFromJson(self.image_path, shape)
        # After removing the shape, update the canvas to reflect the changes
        self.updateCanvas()

    def zoomIn(self):
        self.zoom_factor *= 1.1
        self.applyZoom()

    def zoomOut(self):
        self.zoom_factor *= 0.9
        self.applyZoom()

    def applyZoom(self):
        if self.pixmap.isNull():
            return

        new_width = int(self.pixmap.width() * self.zoom_factor)
        new_height = int(self.pixmap.height() * self.zoom_factor)

        scaled_pixmap = self.pixmap.scaled(new_width, new_height, Qt.KeepAspectRatio)
        self.setPixmap(scaled_pixmap)

    def exportToPng(self):
        if self.pixmap.isNull():
            return

        options = QFileDialog.Options()
        default_filename = f"canvas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Canvas as PNG",
            default_filename,
            "PNG Files (*.png);;All Files (*)",
            options=options
        )

        if file_path:
            writer = QImageWriter(file_path)
            writer.setFormat(QByteArray(b"png"))  # Convert to QByteArray
            writer.write(self.pixmap.toImage()) 
