from qtpy.QtCore import Qt, QMimeData, Signal
from qtpy.QtGui import QDrag, QPixmap, QPaintEvent, QPainter, QCursor
from qtpy.QtWidgets import QWidget, QLabel, QStyle, QStyleOption, QVBoxLayout

class DragTargetIndicator(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContentsMargins(25, 5, 25, 5)
        self.setStyleSheet(
            "QLabel {  border: 3px dotted; text-align: center}"
        )

        self.setText("Drop Here")


class QDragItem(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Store data separately from display label, but use label for default.
        self.data = ""
        self.original_parent = None
        self.original_pos = None

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.original_parent = self.parentWidget()
            self.original_pos = self.pos()
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            self.setCursor(Qt.ClosedHandCursor)
            drag.exec_(Qt.MoveAction)


    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            self.setCursor(Qt.OpenHandCursor)
            drag.exec_(Qt.MoveAction)
            

    def mouseReleaseEvent(self, e):
        self.setCursor(Qt.ArrowCursor)

    def paintEvent(self, event: QPaintEvent):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)



class QDragWidget(QWidget):
    """
    Generic list sorting handler.
    """

    orderChanged = Signal(list)

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setAcceptDrops(True)

        # Initialize layout as None initially
        # self.layout = None

        # Add the drag target indicator. This is invisible by default,
        # we show it and move it around while the drag is active.
        self._drag_target_indicator = DragTargetIndicator()
        self._drag_target_indicator.hide()


    def dragEnterEvent(self, e):
        e.accept()
        self.widgetLayout = self.layout()
        self.widget = e.source()

    def dragLeaveEvent(self, e):
        self._drag_target_indicator.hide()
        self.widget.show()
        e.ignore()
            

    def dragMoveEvent(self, e):
        # Find the correct location of the drop target, so we can move it there.
        index = self.findDropLocation(e)
        if index is not None:
            # Inserting moves the item if its already in the layout.
            self.widgetLayout.insertWidget(index, self._drag_target_indicator)
            # Hide the item being dragged.
            e.source().hide()
            # Show the target.
            self._drag_target_indicator.show()
            # Resize the target indicator to match the size of the widget
            self._drag_target_indicator.setMinimumSize(self.widget.size())
        e.accept()

    def dropEvent(self, e):
        widget = e.source()
        # Use drop target location for destination, then remove it.
        self._drag_target_indicator.hide()
        index = self.widgetLayout.indexOf(self._drag_target_indicator)
        
        # Get the position of the drop event relative to the parent DragWidget
        drop_position = self.mapFromGlobal(QCursor.pos())
        try:
            # Check if the drop event occurred within the bounds of the DragWidget
            if self.rect().contains(drop_position):
                if index == -1:  # Target indicator not found (dropping at the end)
                    index = self.widgetLayout.count()  # Append at the end of the layout
                
                # If index is greater than the length of the layout, append the widget at the end
                if index > self.widgetLayout.count():
                    index = self.widgetLayout.count()
                
                # If the drop was accepted, insert the widget at the drop location.
                self.widgetLayout.insertWidget(index, widget)
                self.orderChanged.emit(self.getItemData())
                widget.show()
                self.widgetLayout.activate()
                
                # Remove the drag target indicator from the layout.
                self.widgetLayout.removeWidget(self._drag_target_indicator)
                
                e.accept()
            else:
                # If the drop occurred outside the DragWidget, return the widget to its original position.
                widget.show()
                e.ignore()
            
            # Ensure the event is only processed once
            e.accept()
    
        except Exception as e:
            print(e)


    def findDropLocation(self, e):
        pos = e.pos()
        spacing = self.widgetLayout.spacing() / 2

        for n in range(self.widgetLayout.count()):
            # Get the widget at each index in turn.
            w = self.widgetLayout.itemAt(n).widget()

            if self.widgetLayout == QVBoxLayout:
                # Drag drop vertically.
                drop_here = (
                    pos.y() >= w.y() - spacing
                    and pos.y() <= w.y() + w.size().height() + spacing
                )
            else:
                # Drag drop horizontally.
                drop_here = (
                    pos.x() >= w.x() - spacing
                    and pos.x() <= w.x() + w.size().width() + spacing
                )

            if drop_here:
                # Drop over this target.
                break

        return n

    def getItemData(self):
        data = []
        for n in range(self.widgetLayout.count()):
            if self.widgetLayout.itemAt(n) is None:
                continue
            # Get the widget at each index in turn.
            w = self.widgetLayout.itemAt(n).widget()
            if hasattr(w, "data"):
                # The target indicator has no data.
                data.append(w.data)
        return data
    
    def paintEvent(self, event: QPaintEvent):
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)