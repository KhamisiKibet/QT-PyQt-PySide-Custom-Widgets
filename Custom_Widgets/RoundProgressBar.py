#############################################################################################
# CREATOR:  ANJAL.P                                                                         #
# ON:       2020 SEP.                                                                       #
# AIM:      To Extend the capability of the PySide2 and PyQt5 Python library with easy to   #
#           use extension containing commonly used widgets which is not natively supported  #
#           by the Qt Frame work (or atleast for Python version of Qt).                     #
# VERSION:  v1.0.0                                                                          #
# NOTES:    CLASS : RoundProgressBar : Can be accessed by : importing                       #
#           from PySide2extn.RoundProgressBar import roundProgressBar                       #
# REFER:    Github:                                                                         #
# DOCUMENTATION:                                                                            #
#############################################################################################

########################################################################
# IMPROVED BY KHAMISI KIBET
# ADOPTED TO WORK WITH THE CUSTOM WIDGETS MODULE
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys

# This import is not used here, if removed sys.modules did not work on my pc
import iconify as ico 

if 'PySide2' in sys.modules:
    from PySide2 import QtWidgets, QtCore
    from PySide2.QtCore import Qt, QSize
    from PySide2.QtGui import QBrush, QColor, QPainter, QPen, QPaintEvent, QFont

elif 'PySide6' in sys.modules:
    from PySide6 import QtWidgets, QtCore
    from PySide6.QtCore import Qt, QSize
    from PySide6.QtGui import QBrush, QColor, QPainter, QPen, QPaintEvent, QFont

else:
    raise Exception("PySide or PySide6 is required, please install it!")

########################################################################
## ROUND PROGRESSBAR
########################################################################
class roundProgressBar(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(roundProgressBar, self).__init__(parent)

        self.positionX = 0 
        self.positionY = 0
        self.posFactor = 0

        self.rpb_minimumSize = (0, 0)
        self.rpb_maximumSize = (0, 0)
        self.rpb_dynamicMin = True
        self.rpb_dynamicMax = True
        self.rpb_Size = 0
        self.sizeFactor = 0

        self.rpb_maximum = 100
        self.rpb_minimum = 0

        self.rpb_type = self.barStyleFlags.Donet
        self.startPosition = self.startPosFlags.North
        self.rpb_direction = self.rotationFlags.Clockwise

        self.rpb_textType = self.textFlags.Percentage
        self.rpb_textColor = (0, 159, 227)
        self.rpb_textWidth = self.rpb_Size/8
        self.rpb_textFont = 'Segoe UI'
        self.rpb_textValue = '12%'
        self.rpb_textRatio = 8
        self.textFactorX = 0
        self.textFactorY = 0
        self.dynamicText = True
        self.rpb_textActive = True

        self.lineWidth = 5
        self.pathWidth = 5
        self.rpb_lineStyle = self.lineStyleFlags.SolidLine
        self.rpb_lineCap = self.lineCapFlags.SquareCap
        self.lineColor = (0, 159, 227)
        self.pathColor = (218, 218, 218)

        self.rpb_circleColor = (218, 218, 218)
        self.rpb_circleRatio = 0.8
        self.rpb_circlePosX = 0
        self.rpb_circlePosY = 0

        self.rpb_pieColor = (200, 200, 200)
        self.rpb_pieRatio = 1
        self.rpb_piePosX = 0
        self.rpb_piePosY = 0

        self.rpb_value = -45*16

        if self.rpb_dynamicMin:
            self.setMinimumSize(QSize(self.lineWidth*6 + self.pathWidth*6, self.lineWidth*6 + self.pathWidth*6))

#------------------------------------------------------CLASS ENUMERATORS
    class lineStyleFlags:
        SolidLine = Qt.SolidLine
        DotLine = Qt.DotLine
        DashLine = Qt.DashLine

    class lineCapFlags:
        SquareCap = Qt.SquareCap
        RoundCap = Qt.RoundCap

    class barStyleFlags:
        Donet = 0
        Line = 1
        Pie = 2
        Pizza = 3
        Hybrid1 = 4
        Hybrid2 = 5

    class rotationFlags:
        Clockwise = -1
        AntiClockwise = 1

    class textFlags:
        Value = 0
        Percentage = 1

    class startPosFlags:
        North = 90*16
        South = -90*16
        East = 0*16
        West = 180*16

#------------------------------------------------------METHODS FOR CHANGING THE PROPERTY OF THE ROUNDPROGRESSBAR :SOLTS

    def rpb_setMinimumSize(self, width, height):
        """
        Minimum Size of the Widget
        ...

        Parameters
        --------------

        width : int
            width of the Widget

        height : int
            height of the Widget

        Raises
        --------------
        Exception : Sorry Width/Height should be an int
        """

        if type(width)!=type(5) or type(height)!=type(5):
            raise Exception('Sorry Width/Height should be an int')
            return
        self.rpb_dynamicMin = False
        self.setMinimumSize(width, height)
        self.rpb_minimumSize = (width, height)
        self.update()

    def rpb_setMaximumSize(self, width, height):
        """
        Maximum Size of the Widget
        ...

        Parameters
        --------------

        width : int
            width of the Widget

        height : int
            height of the Widget

        Raises
        --------------
        Exception : Sorry Width/Height should be an int
        """
        
        if type(width)!=type(5) or type(height)!=type(5):
            raise Exception('Sorry Width/Height should be an int')
            return
        self.rpb_dynamicMax = False
        self.setMaximumSize(width, height)
        self.rpb_maximumSize = (width, height)
        self.update()


    def rpb_setMaximum(self, maximum):
        """
        Maximum Value of the Progressbar
        ...

        Parameters
        --------------

        maximum : int
            Maximum value of the round progress bar

        Raises
        --------------
        Exception : Maximum and Minimum cannot be the Same
        """
        
        if self.rpb_minimum==maximum:               #FOR AVOIDING DIVISION BY ZERO ERROR IN FUTURE
            raise Exception("Maximum and Minimum cannot be the Same")
            return
        if self.rpb_maximum != maximum:
            self.rpb_maximum = maximum
            self.update()

    def rpb_setMinimum(self, minimum):
        """
        Minimum Value of the Progressbar
        ...

        Parameters
        --------------

        minimum : int
            Minimum value of the round progress bar

        Raises
        --------------
        Exception : Maximum and Minimum cannot be the Same
        """
        
        if self.rpb_minimum==maximum:               #FOR AVOIDING DIVISION BY ZERO ERROR IN FUTURE
            raise Exception("Maximum and Minimum cannot be the Same")
            return
        if self.rpb_minimum != minimum:
            self.rpb_minimum = minimum
            self.update()

    def rpb_setRange(self, maximum, minimum):
        """
        Range include the maximum and the minimum in one go.
        ...

        Parameters
        --------------

        maximum : int
            Maximum value of the round progress bar

        minimum : int
            Minimum value for the round progress bar

        Raises
        --------------
        none
        """
        
        if minimum > maximum:
            maximum, minimum = minimum, maximum
        if self.rpb_maximum != maximum:
            self.rpb_maximum = maximum
        if self.rpb_minimum != minimum:
            self.rpb_minimum = minimum
        self.update()

    def rpb_setInitialPos(self, pos):
        """
        Starting position of the round progress bar
        ...

        Parameters
        --------------

        pos : String
            Position string: 'North', 'South', 'East' and 'West'

        Raises
        --------------
        ValueError : Maximum and Minimum cannot be the Same
        """
        
        if pos=='North':
            self.startPosition = self.startPosFlags.North
        elif pos=='South':
            self.startPosition = self.startPosFlags.South
        elif pos=='East':
            self.startPosition = self.startPosFlags.East
        elif pos=='West':
            self.startPosition = self.startPosFlags.West
        else:
            raise Exception("Initial Position String can be: 'South', 'North'")
            return

    def rpb_setValue(self, value):
        """
        Set progress value
        ...

        Parameters
        --------------

        value : int
            The value of the progress bar in int. The value should be: min<=value<=max

        Raises
        --------------
        none
        """
        
        if self.rpb_value != value:
            if value >= self.rpb_maximum:
                roundProgressBar.convertInputValue(self, self.rpb_maximum)
            elif value < self.rpb_minimum:
                roundProgressBar.convertInputValue(self, self.rpb_minimum)
            else:
                roundProgressBar.convertInputValue(self, value)
            self.update()

    def rpb_reset(self):
        """
        Reset the progress bar to 0%
        ...

        Parameters
        --------------
        none

        Raises
        --------------
        none
        """
        
        roundProgressBar.convertInputValue(self, self.rpb_minimum)
        self.update()

    def rpb_setGeometry(self, posX, posY):
        """
        Set the X and Y position of the round progress bar.
        ...

        Parameters
        --------------

        posX : int
            The position of the round progress bar in int for X axis.

        posY : int
            The position of the round progress bar in int for Y axis.

        Raises
        --------------
        none
        """
        
        if self.positionX != posX:
            self.positionX = posX
        if self.positionY != posY:
            self.positionY = posY
        self.update()

    def rpb_setLineWidth(self, width):
        """
        Line Width of the line in round progress bar.
        ...

        Parameters
        --------------

        width: int
            Line width corresponding to the width in px.

        Raises
        --------------
        Exception: Line Width should be in int
        """

        if type(width)!=type(5):
            raise Exception('Line Width should be in int')
            return
        if self.lineWidth != width:
            self.lineWidth = width
            self.update()

    def rpb_setLineColor(self, rgb):
        """
        Line Color of the progress bar.
        ...

        Parameters
        --------------

        rgb: tuple: (R, G, B)
            Color is passed as a tuple of values for red, blue and green in the order: (R, G, B)

        Raises
        --------------
        Exception: Line Color accepts a tuple: (R, G, B).
        """

        if type(rgb)!=type(()):
            raise Exception("Line Color accepts a tuple: (R, G, B).")
            return
        if self.lineColor != rgb:
            self.lineColor = rgb
            self.update()

    def rpb_setPathColor(self, rgb):
        """
        Path Color settings.
        ...

        Parameters
        --------------

        rgb: tuple: (R, G, B)
            Color is passed as a tuple of values for red, blue and green in the order: (R, G, B)

        Raises
        --------------
        Exception: Path Color accepts a tuple: (R, G, B).
        """
        
        if type(rgb)!=type(()):
            raise Exception("Path Color accepts a tuple: (R, G, B).")
            return
        if self.pathColor != rgb:
            self.pathColor = rgb
            self.update()

    def rpb_setPathWidth(self, width):
        """
        Path width settings.
        ...

        Parameters
        --------------

        width: int
            Width of the path in px

        Raises
        --------------
        Exception: Line Width should be in int
        """

        if type(width)!=type(5):
            raise Exception('Path Width should be in int')
            return
        if self.pathWidth != width:
            self.pathWidth = width
            self.update()

    def rpb_setDirection(self, direction):
        """
        Direction of rotation of the progress bar.
        ...

        Parameters
        --------------

        direction: string
            string can be: 'AntiClockwise' or 'Clockwise'. Default: 'Clockwise'.

        Raises
        --------------
        Exception: Direction can only be: 'Clockwise' and 'AntiClockwise'
        """

        if direction == 'Clockwise' or direction == -1:
            self.rpb_direction = self.rotationFlags.Clockwise
        elif direction == 'AntiClockwise' or direction == 1:
            self.rpb_direction = self.rotationFlags.AntiClockwise
        else:
            raise Exception("Direction can only be: 'Clockwise' and 'AntiClockwise' and Not: " + str(direction))
            return
        self.update()

    def rpb_setBarStyle(self, style):
        """
        Bar Style of the progress bar.
        ...

        Parameters
        --------------

        style: String
            String of the styles of the progress bar: 'Donet', 'Pie', 'line', 'Hybrid1', 'Hybrid2', 'Pizza'

        Raises
        --------------
        Exception: Round Progress Bar has only the following styles: 'Line', 'Donet', 'Hybrid1', 'Pizza', 'Pie' and 'Hybrid2'
        """

        if style=='Donet':
            self.rpb_type = self.barStyleFlags.Donet
        elif style=='Line':
            self.rpb_type = self.barStyleFlags.Line
        elif style=='Pie':
            self.rpb_type = self.barStyleFlags.Pie
        elif style=='Pizza':
            self.rpb_type = self.barStyleFlags.Pizza
        elif style=='Hybrid1':
            self.rpb_type = self.barStyleFlags.Hybrid1
        elif style=='Hybrid2':
            self.rpb_type = self.barStyleFlags.Hybrid2
        else:
            raise Exception("Round Progress Bar has only the following styles: 'Line', 'Donet', 'Hybrid1', 'Pizza', 'Pie' and 'Hybrid2'")
            return
        self.update()

    def rpb_setLineStyle(self, style):
        """
        Line Style setting.
        ...

        Parameters
        --------------

        style: String
            Line style: 'DotLine', 'DashLine', 'SolidLine', passed as a string.

        Raises
        --------------
        none
        """

        if style == 'SolidLine':
            self.rpb_lineStyle = self.lineStyleFlags.SolidLine
        elif style == 'DotLine':
            self.rpb_lineStyle = self.lineStyleFlags.DotLine
        elif style == 'DashLine':
            self.rpb_lineStyle = self.lineStyleFlags.DashLine
        else:
            self.rpb_lineStyle = self.lineStyleFlags.SolidLine

    def rpb_setLineCap(self, cap):
        """
        Line Cap setting.
        ...

        Parameters
        --------------

        cap: String
            Cap is the end point of a stroke. It can be: 'RoundCap' or 'SquareCap'

        Raises
        --------------
        none
        """

        if cap=='SquareCap':
            self.rpb_lineCap = self.lineCapFlags.SquareCap
        elif cap == 'RoundCap':
            self.rpb_lineCap = self.lineCapFlags.RoundCap

    def rpb_setTextColor(self, rgb):
        """
        Text color of the text inside the progress bar
        ...

        Parameters
        --------------

        rgb: tuple
            Color of the text in the format: (R, G, B)

        Raises
        --------------
        none
        """

        if self.rpb_textColor != rgb:
            self.rpb_textColor = rgb
            self.update()

    def rpb_setTextFont(self, font):
        """
        Font of the text inside the round progress bar
        ...

        Parameters
        --------------

        font: str
            Name of the font in string

        Raises
        --------------
        none
        """

        if self.rpb_textFont != font:
            self.rpb_textFont = font
            self.update()

    def rpb_setTextFormat(self, textTyp):
        """
        Text formatter i.e. the value or the percentage.
        ...

        Parameters
        --------------

        textTyp: str
            'value', 'percentage'

        Raises
        --------------
        none
        """

        if textTyp == 'Value':
            self.rpb_textType = self.textFlags.Value
        elif textTyp == 'Percentage':
            self.rpb_textType = self.textFlags.Percentage
        else:
            self.rpb_textType = self.textFlags.Percentage

    def rpb_setTextRatio(self, ratio):
        """
        Text ratio with respect to the size of the progress bar.
        ...

        Parameters
        --------------

        ratio: int
            In number from 3 to 50 corresponding to 1/3 or 1/50 the size of the roundprogressbar.

        Raises
        --------------
        none
        """

        if self.rpb_textRatio != ratio:
            if ratio < 3:
                ratio = 3
            elif ratio > 50:
                ratio = 50
            self.rpb_textRatio = ratio
            self.update()

    def rpb_setTextWidth(self, width):
        """
        Text Width.
        ...

        Parameters
        --------------

        font: int
            Text constant width. Will not change during the widget resize.

        Raises
        --------------
        none
        """

        self.dynamicText = False
        if width > 0:
            self.rpb_textWidth = width
            self.update()

    def rpb_setCircleColor(self, rgb):
        """
        Circle color fill inside the circle.
        ...

        Parameters
        --------------

        font: tuple
            The color of the circle in the tuple corresponding to the (R, G, B).

        Raises
        --------------
        none
        """

        if self.rpb_circleColor != rgb:
            self.rpb_circleColor = rgb
            self.update()

    def rpb_setCircleRatio(self, ratio):
        """
        Circle ration corresponding to the round progress bar.
        ...

        Parameters
        --------------

        font: int
            Integer corresponding to the size of the progress bar to that of the round progress bar.

        Raises
        --------------
        none
        """

        if self.rpb_circleRatio != ratio:
            self.rpb_circleRatio = ratio
            self.update()

    def rpb_setPieColor(self, rgb):
        """
        Pie color inside the fill.
        ...

        Parameters
        --------------

        font: tuple
            Tuple consist in format (R, G, B). Same as color setting to Line.

        Raises
        --------------
        none
        """

        if self.rpb_pieColor != rgb:
            self.rpb_pieColor = rgb
            self.update()

    def rpb_setPieRatio(self, ratio):
        """
        Pie Ratio
        ...

        Parameters
        --------------

        font: int
            Ratio corresponding to the size between the roundprogressbar and the pie size.

        Raises
        --------------
        none
        """

        if self.rpb_pieRatio != ratio:
            self.rpb_pieRatio = ratio
            self.update()

    def rpb_enableText(self, enable):
        """
        Makes the Text visible/Hidden
        ...

        Parameters
        --------------

        font: bool
            True: Text visible, False: Text invisible.

        Raises
        --------------
        none
        """

        if enable:
            self.rpb_textActive = enable
        else:
            self.rpb_textActive = enable
        self.update()


#------------------------------------------------------METHODS FOR GETTING THE PROPERTY OF ROUNDPROGRESSBAR SLOTS

    def rpb_getSize(self):
        """
        Get the present size of the progress bar.
        ...

        Returns
        --------------
        Return the size of the round progress bar in int.
        """

        return self.rpb_Size

    def rpb_getValue(self):
        """
        Present value of the progress bar.
        ...

        Returns
        --------------
        int corresponding to the present progress bar value.
        """

        return self.rpb_value/16

    def rpb_getRange(self):
        """
        Progress bar range.
        ...

        Returns
        --------------
        tuple consisting of minimu and maximum as elements.
        """

        return (self.rpb_minimum, self.rpb_maximum)

    def rpb_getTextWidth(self):
        """
        Text width of the present text in the central of the widget.
        ...

        Returns
        --------------
        int corresponding to the width of the text
        """

        return self.rpb_textWidth

#------------------------------------------------------ENGINE: WHERE ALL THE REAL STUFF TAKE PLACE: WORKING OF THE ROUNDPROGRESSBA

    def rpb_MinimumSize(self, dynamicMax, minimum, maximum):
        """
        Minimum size calculating code: Takes consideration of the width of the line/path/circle/pie and the user defined
        width and also the size of the frame/window of the application.

        """

        rpb_Height = self.height()
        rpb_Width = self.width()
        if dynamicMax:
            if rpb_Width >= rpb_Height and rpb_Height >= minimum[1]:
                self.rpb_Size = rpb_Height
            elif rpb_Width < rpb_Height and rpb_Width >= minimum[0]:
                self.rpb_Size = rpb_Width
        else:
            if rpb_Width >= rpb_Height and rpb_Height <= maximum[1]:
                self.rpb_Size = rpb_Height
            elif rpb_Width < rpb_Height and rpb_Width <= maximum[0]:
                self.rpb_Size = rpb_Width

    def convertInputValue(self, value):
        """
        CONVERTS ANY INPUT VALUE TO THE 0*16-360*16 DEGREE REFERENCE OF THE QPainter.drawArc NEEDED.

        """

        self.rpb_value = ((value - self.rpb_minimum)/(self.rpb_maximum - self.rpb_minimum))*360*16
        self.rpb_value = self.rpb_direction*self.rpb_value
        if self.rpb_textType==roundProgressBar.textFlags.Percentage:
            self.rpb_textValue = str(round(((value - self.rpb_minimum)/(self.rpb_maximum - self.rpb_minimum))*100)) + "%"
        else:
            self.rpb_textValue = str(value)

    #SINCE THE THICKNESS OF THE LINE OR THE PATH CAUSES THE WIDGET TO WRONGLY FIT INSIDE THE SIZE OF THE WIDGET DESIGNED IN THE 
    #QTDESIGNER, THE CORRECTION FACTOR IS NECESSERY CALLED THE GEOMETRYFACTOR, WHICH CALCULATE THE TWO FACTORS CALLED THE
    #self.posFactor AND THE self.sizeFactor, CALCULATION THIS IS NECESSERY AS THE 
    def geometryFactor(self):
        if self.lineWidth > self.pathWidth:
            self.posFactor = self.lineWidth/2 + 1
            self.sizeFactor = self.lineWidth + 1
        else:
            self.posFactor = self.pathWidth/2 + 1
            self.sizeFactor = self.pathWidth + 1

    def rpb_textFactor(self):
        if self.dynamicText:
            self.rpb_textWidth = self.rpb_Size/self.rpb_textRatio
        self.textFactorX = self.posFactor + (self.rpb_Size - self.sizeFactor)/2 - self.rpb_textWidth*0.75*(len(self.rpb_textValue)/2)
        self.textFactorY = self.rpb_textWidth/2 + self.rpb_Size/2

    def rpb_circleFactor(self):
        self.rpb_circlePosX = self.positionX + self.posFactor +  ((self.rpb_Size)*(1 - self.rpb_circleRatio))/2
        self.rpb_circlePosY = self.positionY + self.posFactor + ((self.rpb_Size)*(1 - self.rpb_circleRatio))/2

    def rpb_pieFactor(self):
        self.rpb_piePosX = self.positionX + self.posFactor +  ((self.rpb_Size)*(1 - self.rpb_pieRatio))/2
        self.rpb_piePosY = self.positionY + self.posFactor + ((self.rpb_Size)*(1 - self.rpb_pieRatio))/2



    def paintEvent(self, event: QPaintEvent):
        
        #THIS BELOW CODE AMKE SURE THAT THE SIZE OF THE ROUNDPROGRESSBAR DOESNOT REDUCES TO ZERO WHEN THE USER RESIZES THE WINDOW
        if self.rpb_dynamicMin:
            self.setMinimumSize(QSize(self.lineWidth*6 + self.pathWidth*6, self.lineWidth*6 + self.pathWidth*6))

        roundProgressBar.rpb_MinimumSize(self, self.rpb_dynamicMax, self.rpb_minimumSize, self.rpb_maximumSize)
        roundProgressBar.geometryFactor(self)
        roundProgressBar.rpb_textFactor(self)
        roundProgressBar.rpb_circleFactor(self)
        roundProgressBar.rpb_pieFactor(self)
        
        if self.rpb_type==0: #DONET TYPE
            roundProgressBar.pathComponent(self)
            roundProgressBar.lineComponent(self)
            roundProgressBar.textComponent(self)
        elif self.rpb_type==1: #LINE TYPE
            roundProgressBar.lineComponent(self)
            roundProgressBar.textComponent(self)
        elif self.rpb_type==2: #Pie
            roundProgressBar.pieComponent(self)
            roundProgressBar.textComponent(self)
        elif self.rpb_type==3: #PIZZA
            roundProgressBar.circleComponent(self)
            roundProgressBar.lineComponent(self)
            roundProgressBar.textComponent(self)
        elif self.rpb_type==4: #HYBRID1
            roundProgressBar.circleComponent(self)
            roundProgressBar.pathComponent(self)
            roundProgressBar.lineComponent(self)
            roundProgressBar.textComponent(self)
        elif self.rpb_type==5: #HYBRID2
            roundProgressBar.pieComponent(self)
            roundProgressBar.lineComponent(self)
            roundProgressBar.textComponent(self)

        
    def lineComponent(self):
        linePainter = QPainter(self)
        linePainter.setRenderHint(QPainter.Antialiasing)
        penLine = QPen()
        penLine.setStyle(self.rpb_lineStyle)
        penLine.setWidth(self.lineWidth)
        penLine.setBrush(QColor(self.lineColor[0], self.lineColor[1], self.lineColor[2]))
        penLine.setCapStyle(self.rpb_lineCap)
        penLine.setJoinStyle(Qt.RoundJoin)
        linePainter.setPen(penLine)
        linePainter.drawArc(self.positionX + self.posFactor, self.positionY + self.posFactor, self.rpb_Size - self.sizeFactor, self.rpb_Size - self.sizeFactor, self.startPosition, self.rpb_value)
        linePainter.end()

    def pathComponent(self):
        pathPainter = QPainter(self)
        pathPainter.setRenderHint(QPainter.Antialiasing)
        penPath = QPen()
        penPath.setStyle(Qt.SolidLine)
        penPath.setWidth(self.pathWidth)
        penPath.setBrush(QColor(self.pathColor[0], self.pathColor[1], self.pathColor[2]))
        penPath.setCapStyle(Qt.RoundCap)
        penPath.setJoinStyle(Qt.RoundJoin)
        pathPainter.setPen(penPath)
        pathPainter.drawArc(self.positionX + self.posFactor, self.positionY + self.posFactor, self.rpb_Size - self.sizeFactor, self.rpb_Size - self.sizeFactor, 0, 360*16)
        pathPainter.end()

    def textComponent(self):
        if self.rpb_textActive:
            textPainter = QPainter(self)
            penText = QPen()
            penText.setColor(QColor(self.rpb_textColor[0], self.rpb_textColor[1], self.rpb_textColor[2]))
            textPainter.setPen(penText)
            fontText = QFont()
            fontText.setFamily(self.rpb_textFont)
            fontText.setPointSize(self.rpb_textWidth)
            textPainter.setFont(fontText)
            textPainter.drawText(self.positionX + self.textFactorX, self.positionY + self.textFactorY, self.rpb_textValue)
            textPainter.end()

    def circleComponent(self):
        circlePainter = QPainter(self)   
        penCircle = QPen()
        penCircle.setWidth(0)
        penCircle.setColor(QColor(self.rpb_circleColor[0], self.rpb_circleColor[1], self.rpb_circleColor[2]))
        circlePainter.setRenderHint(QPainter.Antialiasing)
        circlePainter.setPen(penCircle)
        circlePainter.setBrush(QColor(self.rpb_circleColor[0], self.rpb_circleColor[1], self.rpb_circleColor[2]))
        circlePainter.drawEllipse(self.rpb_circlePosX, self.rpb_circlePosY, (self.rpb_Size - self.sizeFactor)*self.rpb_circleRatio, (self.rpb_Size - self.sizeFactor)*self.rpb_circleRatio)

    def pieComponent(self):
        piePainter = QPainter(self)   
        penPie = QPen()
        penPie.setWidth(0)
        penPie.setColor(QColor(self.rpb_pieColor[0], self.rpb_pieColor[1], self.rpb_pieColor[2]))
        piePainter.setRenderHint(QPainter.Antialiasing)
        piePainter.setPen(penPie)
        piePainter.setBrush(QColor(self.rpb_pieColor[0], self.rpb_pieColor[1], self.rpb_pieColor[2]))
        piePainter.drawPie(self.rpb_piePosX, self.rpb_piePosY, (self.rpb_Size - self.sizeFactor)*self.rpb_pieRatio, (self.rpb_Size - self.sizeFactor)*self.rpb_pieRatio, self.startPosition, self.rpb_value)


#------------------------------------------------------

if __name__=="__main__":
    print("Try Import.")