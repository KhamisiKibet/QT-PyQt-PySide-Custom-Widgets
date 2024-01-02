"""
The primary objects for interfacing with iconify
"""

from typing import TYPE_CHECKING, MutableMapping, Optional, Tuple

from Custom_Widgets.iconify.anim import GlobalTick
from Custom_Widgets.iconify.path import findIcon
from Custom_Widgets.iconify.qt import QtCore, QtGui, QtSvg

if TYPE_CHECKING:
    from Custom_Widgets.iconify.anim import BaseAnimation
    from Custom_Widgets.iconify.qt import QtWidgets
    PixmapCacheKey = Tuple[Optional[str], QtCore.QSize, str, int, int]


class Icon(QtGui.QIcon):
    """
    The Iconify Icon which renders an svg image
    using the provided color & anim.
    """

    def __new__(
        cls,
        path,  # type: str
        color=None,  # type: Optional[QtGui.QColor]
        anim=None  # type: Optional[BaseAnimation]
    ):
        # type: (...) -> QtGui.QIcon
        """
        Return a QtGui.QIcon with extra convenience methods patched onto it.

        Patching a QIcon, rather than subclassing it, is required for the
        object to work correctly with Qt's model / view framework.

        Parameters
        ----------
        path : str
        color : Optional[QtGui.QColor]
        anim : Optional[BaseAnimation]

        Returns
        -------
        QtGui.QIcon
        """
        iconEngine = _IconEngine(path, color=color, anim=anim)
        icon = QtGui.QIcon(iconEngine)

        def _setAsButtonIcon(button):
            # type: (QtWidgets.QAbstractButton) -> None
            button.setIcon(icon)
            if iconEngine.animCount() > 1:
                GlobalTick.timeout.connect(button.update)
            else:
                if anim is not None:
                    anim.tick.connect(button.update)

        icon.setAsButtonIcon = _setAsButtonIcon
        icon.addState = iconEngine.addState
        icon.pixmapGenerator = iconEngine.pixmapGenerator
        icon.color = iconEngine.color
        icon.anim = iconEngine.anim
        icon.animCount = iconEngine.animCount
        return icon


class _IconEngine(QtGui.QIconEngine):
    """
    A QIconEngine which uses a PixmapGenerator for it's work.
    """

    def __init__(self, path, color=None, anim=None):
        # type: (str, Optional[QtGui.QColor], Optional[BaseAnimation]) -> None
        super(_IconEngine, self).__init__()
        self._defaultGenerator = PixmapGenerator(path, color=color, anim=anim)
        self._pixmapGenerators = {(QtGui.QIcon.Normal, QtGui.QIcon.Off):
                                  self._defaultGenerator}

    def __del__(self):
        # type: () -> None
        """
        Re-implemented to avoid this object being
        garbage collected unnecessarily.
        """

    def addState(
        self,
        path,  # type: str
        color=None,  # type: Optional[QtGui.QColor]
        anim=None,  # type: Optional[BaseAnimation]
        mode=QtGui.QIcon.Normal,  # type: QtGui.QIcon.Mode
        state=QtGui.QIcon.Off  # type: QtGui.QIcon.State
    ):
        # type: (...) -> None
        """
        Use the provided path, color and animation when an icon is requested
        for the identified mode and state.

        Parameters
        ----------
        path : str
        color : Optional[QtGui.QColor]
        anim : Optional[BaseAnimation]
        mode : QtGui.QIcon.Mode
        state : QtGui.QIcon.Stat
        """
        color = color or self.color()
        anim = anim or self.anim()
        generator = PixmapGenerator(path, color=color, anim=anim)
        self._pixmapGenerators[(mode, state)] = generator

    def pixmapGenerator(self, mode=QtGui.QIcon.Normal, state=QtGui.QIcon.Off):
        # type: (QtGui.QIcon.Mode, QtGui.QIcon.State) -> PixmapGenerator
        """
        Return the PixmapGenerator to use for the provided mode & state.

        If no PixmapGenerator has been defined for the provided mode & state
        combination, the PixmapGenerator created in the constructor is used.

        Parameters
        ----------
        mode : QtGui.QIcon.Mode
        state : QtGui.QIcon.State

        Returns
        -------
        PixmapGenerator
        """
        return self._pixmapGenerators.get(
            (mode, state),
            self._defaultGenerator,
        )

    def anim(
        self,
        mode=QtGui.QIcon.Normal,  # type: QtGui.QIcon.Mode
        state=QtGui.QIcon.Off,  # type: QtGui.QIcon.State
    ):
        # type: (...) -> Optional[BaseAnimation]
        """
        Return the animation used for the provided mode & state.

        Parameters
        ----------
        mode : QtGui.QIcon.Mode
        state : QtGui.QIcon.State

        Returns
        -------
        Optional[BaseAnimation]
        """
        return self.pixmapGenerator(mode=mode, state=state).anim()

    def animCount(self):
        # type: () -> int
        """
        Return the number of animations that are associated with the available
        states of this icon engine.

        Returns
        -------
        int
        """
        animCount = 0
        for pixmapGenerator in self._pixmapGenerators.values():
            if pixmapGenerator.anim() is not None:
                animCount += 1
        return animCount

    def color(
        self,
        mode=QtGui.QIcon.Normal,  # type: QtGui.QIcon.Mode
        state=QtGui.QIcon.Off,  # type: QtGui.QIcon.State
    ):
        # type: (...) -> Optional[QtGui.QColor]
        """
        Return the color used for the provided mode & state.

        Parameters
        ----------
        mode : QtGui.QIcon.Mode
        state : QtGui.QIcon.State

        Returns
        -------
        Optional[BaseAnimation]
        """
        return self.pixmapGenerator(mode=mode, state=state).color()

    def pixmap(
        self,
        size,  # type: QtCore.QSize
        mode,  # type: QtGui.QIcon.Mode
        state,  # type: QtGui.QIcon.State
    ):
        # type: (...) -> QtGui.QPixmap
        """
        Return a QPixmap to use for the identified mode & state, rendered at
        the provided size.

        Parameters
        ----------
        size : QtCore.QSize
        mode : QtGui.QIcon.Mode
        state : QtGui.QIcon.State

        Returns
        -------
        QtGui.QPixmap
        """
        return self.pixmapGenerator(mode=mode, state=state).pixmap(size)

    def paint(
        self,
        painter,  # type: QtCore.QPainter
        rect,  # type: QtCore.QRect
        mode,  # type: QtGui.QIcon.Mode
        state,  # type: QtGui.QIcon.State
    ):
        # type: (...) -> None
        painter.drawPixmap(
            rect.topLeft(), self.pixmap(rect.size(), mode, state)
        )


class PixmapGenerator(QtCore.QObject):
    """
    Responsible for rendering the svg image and applying the color and
    transform from the animation during the process.

    It's backed by a cache to ensure that redundant rendering does not happen.
    """

    _pixmapCache = {}  # type: MutableMapping[PixmapCacheKey, QtGui.QPixmap]

    def __init__(
        self,
        path,  # type: str
        color=None,  # type: Optional[QtGui.QColor]
        anim=None,  # type: Optional[BaseAnimation]
        parent=None,  # type: Optional[QtCore.QObject]
    ):
        # type: (...) -> None
        super(PixmapGenerator, self).__init__(parent=parent)
        self._path = findIcon(path)
        self._color = color  # type: Optional[QtGui.QColor]
        self._anim = anim  # type: Optional[BaseAnimation]

        self._renderer = QtSvg.QSvgRenderer(self._path)

    def path(self):
        # type: () -> str
        """
        Return the path to the image used by this PixmapGenerator.

        Returns
        -------
        str
        """
        return self._path

    def color(self):
        # type: () -> Optional[QtGui.QColor]
        """
        Return the color used by this PixmapGenerator.

        Returns
        -------
        Optional[QtGui.QColor]
        """
        return self._color

    def anim(self):
        # type: () -> Optional[BaseAnimation]
        """
        Return the animation used by this PixmapGenerator.

        Returns
        -------
        Optional[BaseAnimation]
        """
        return self._anim

    def pixmap(self, size):
        # type: (QtCore.QSize) -> QtGui.QPixmap
        """
        Render the svg file to a QPixmap, applying the color override and the
        animation transform if applicable.

        Parameters
        ----------
        size : QtCore.QSize

        Returns
        -------
        QtGui.QPixmap
        """
        color = self._color.rgb() if self._color else -1

        if self._anim is not None:
            key = (
                self._path, size, str(self._anim.__class__),
                self._anim.frame(), color
            )  # type: PixmapCacheKey
        else:
            key = (self._path, size, "", 0, color)

        if key in self._pixmapCache:
            return self._pixmapCache[key]

        image = QtGui.QImage(
            size,
            QtGui.QImage.Format_ARGB32_Premultiplied,
        )
        image.fill(QtCore.Qt.transparent)

        # Use the QSvgRenderer to draw the image
        painter = QtGui.QPainter(image)

        if self._anim:
            # Rotate the painter's co-ordinate space so
            # the image is correctly positioned.
            xfm = self._anim.transform(size)
            painter.setTransform(xfm)

        self._renderer.render(painter)
        painter.end()

        if self._color is not None:
            # Use the alpha channel on a solid colour image
            colorImage = QtGui.QImage(
                size,
                QtGui.QImage.Format_ARGB32_Premultiplied,
            )
            colorImage.fill(QtGui.QColor(self._color))
            try:
                colorImage.setAlphaChannel(image.alphaChannel())
            except AttributeError:
                if image.hasAlphaChannel():
                    colorImage.setAlphaChannel(image)

            image = colorImage

        pixmap = QtGui.QPixmap.fromImage(image)
        self._pixmapCache[key] = pixmap
        return pixmap
