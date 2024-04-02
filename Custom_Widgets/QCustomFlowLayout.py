from qtpy import QtGui, QtCore, QtWidgets
import typing

# https://github.com/baoboa/pyqt5/blob/master/examples/layouts/flowlayout.py
class QCustomFlowLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super().__init__(parent)

        if parent is not None:
            self.setContentsMargins(margin, margin, margin, margin)

        self.setSpacing(spacing)

        self._items = []
        self.__pending_positions = {}

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, a0: QtWidgets.QLayoutItem) -> None:
        try:
            position = self.__pending_positions[a0.widget()]
            self._items.insert(position, a0)
            del self.__pending_positions[a0.widget()]
        except KeyError:
            self._items.append(a0)

    def addWidget(self, w: QtWidgets.QWidget, position: int = None, align: QtCore.Qt.AlignmentFlag = None) -> None:
        if position is not None:
            self.__pending_positions[w] = position
        if align is not None:
            frame_layout = w.layout()
            if frame_layout is not None:
                frame_layout.setAlignment(align)
        super().addWidget(w)

    def count(self):
        return len(self._items)

    def expandingDirections(self):
        return QtCore.Qt.Orientations(QtCore.Qt.Orientation(0))

    def itemAt(self, index: int) -> QtWidgets.QLayoutItem:
        if 0 <= index < len(self._items):
            return self._items[index]

        return None

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self._doLayout(QtCore.QRect(0, 0, width, 0), True)
        return height

    def minimumSize(self):
        size = QtCore.QSize()

        for item in self._items:
            size = size.expandedTo(item.minimumSize())

        margin, _, _, _ = self.getContentsMargins()

        size += QtCore.QSize(2 * margin, 2 * margin)
        return size

    def removeItem(self, a0: QtWidgets.QLayoutItem) -> None:
        a0.widget().deleteLater()

    def removeWidget(self, w: QtWidgets.QWidget) -> None:
        w.deleteLater()

    def setGeometry(self, rect):
        super().setGeometry(rect)
        self._doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def takeAt(self, index: int) -> QtWidgets.QLayoutItem:
        if 0 <= index < len(self._items):
            return self._items.pop(index)

        return None

    def _doLayout(self, rect, testOnly):
        """This does the layout. Dont ask me how. Source: https://github.com/baoboa/pyqt5/blob/master/examples/layouts/flowlayout.py"""
        x = rect.x()
        y = rect.y()
        line_height = 0

        for item in self._items:
            wid = item.widget()
            space_x = self.spacing() + wid.style().layoutSpacing(
                QtWidgets.QSizePolicy.PushButton,
                QtWidgets.QSizePolicy.PushButton,
                QtCore.Qt.Horizontal)
            space_y = self.spacing() + wid.style().layoutSpacing(
                QtWidgets.QSizePolicy.PushButton,
                QtWidgets.QSizePolicy.PushButton,
                QtCore.Qt.Vertical)
            next_x = x + item.sizeHint().width() + space_x
            if next_x - space_x > rect.right() and line_height > 0:
                x = rect.x()
                y = y + line_height + space_y
                next_x = x + item.sizeHint().width() + space_x
                line_height = 0

            if not testOnly:
                item.setGeometry(QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))

            x = next_x
            line_height = max(line_height, item.sizeHint().height())

        return y + line_height - rect.y()
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._doLayout(self.geometry(), False)