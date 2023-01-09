#############################################################################################
# CREATOR:  ANJAL.P                                                                         #
# ON:       2020 NOV.                                                                       #
# AIM:      To Extend the capability of the PySide2 and PyQt5 Python library with easy to   #
#           use extension containing commonly used widgets which is not natively supported  #
#           by the Qt Frame work (or atleast for Python version of Qt).                     #
# VERSION:  v1.0.0                                                                          #
# NOTES:    CLASS : SpiralProgressBar : Can be accessed by : importing                      #
#           from PySide2extn.SpiralProgressBar import spiralProgressBar                     #
# REFER:    Github:                                                                         #
# DOCUMENTATION:                                                                            #
#############################################################################################

########################################################################
## IMPORT PYSIDE2 OR PYSIDE6
########################################################################
# if 'PySide2' in sys.modules:
#     from PySide2 import QtWidgets, QtCore
#     from PySide2.QtCore import Qt, QSize
#     from PySide2.QtGui import QBrush, QColor, QPainter, QPen, QPaintEvent, QFont

# elif 'PySide6' in sys.modules:
#     from PySide6 import QtWidgets, QtCore
#     from PySide6.QtCore import Qt, QSize
#     from PySide6.QtGui import QBrush, QColor, QPainter, QPen, QPaintEvent, QFont

# else:
#     raise Exception("PySide2 or PySide6 is required, please install it!")

########################################################################
## MODULE UPDATED TO USE QTPY
########################################################################
from qtpy import QtWidgets, QtCore
from qtpy.QtCore import Qt, QSize
from qtpy.QtGui import QBrush, QColor, QPainter, QPen, QPaintEvent, QFont


class spiralProgressBar(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(spiralProgressBar, self).__init__(parent)

        self.positionX = 0 
        self.positionY = 0
        self.spb_Size = 0
        self.posFactor = 0
        self.sizeFactor = 0

        self.spb_maximSize = (0, 0)
        self.spb_minimSize = (0, 0)

        self.spb_dynamicMin = True
        self.spb_dynamicMax = True

        self.noProgBar = 3

        self.spb_value = [-48*16, -24*16, -12*16]
        self.spb_minimValue = [0, 0, 0]
        self.spb_maximValue = [100, 100, 100]
        self.spb_startPos = [self.startPosFlags.North, self.startPosFlags.North, self.startPosFlags.North]
        self.spb_direction = [self.rotationFlags.Clockwise, self.rotationFlags.Clockwise, self.rotationFlags.Clockwise]

        self.lineWidth = 5
        self.lineColor = [[0, 159, 227], [0, 159, 227], [0, 159, 227]]
        self.lineStyle = [self.lineStyleFlags.SolidLine, self.lineStyleFlags.SolidLine, self.lineStyleFlags.SolidLine]
        self.lineCap = [self.lineCapFlags.RoundCap, self.lineCapFlags.RoundCap, self.lineCapFlags.RoundCap]
        self.varWidth = False
        self.widthIncr = 1
        
        self.pathWidth = 5
        self.pathColor = [[179, 241, 215], [179, 241, 215], [179, 241, 215]]
        self.pathPresent = True
        self.pathStyle = [self.lineStyleFlags.SolidLine, self.lineStyleFlags.SolidLine, self.lineStyleFlags.SolidLine]
        self.pathIndepend = False

        self.spb_gap = self.lineWidth*2   #GAP BETWEEN THE ROUNDPROGRESS BAR MAKING A SPIRAL PROGRESS BAR.
        self.gapCngd = False
        self.spb_cngSize = 1

#------------------------------------------------------CLASS ENUMERATORS
    class lineStyleFlags:
        SolidLine = Qt.SolidLine
        DotLine = Qt.DotLine
        DashLine = Qt.DashLine

    class lineCapFlags:
        SquareCap = Qt.SquareCap
        RoundCap = Qt.RoundCap

    class rotationFlags:
        Clockwise = -1
        AntiClockwise = 1

    class startPosFlags:
        North = 90*16
        South = -90*16
        East = 0*16
        West = 180*16

#------------------------------------------------------METHODS FOR CHANGING THE PROPERTY OF THE SPIRALPROGRESSBAR :SOLTS

    def spb_setMinimumSize(self, width, height):
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
        none
        """
        self.spb_dynamicMin = False
        self.setMinimumSize(width, height)
        self.spb_minimSize = (width, height)
        self.update()


    def spb_setMaximumSize(self, width, height):
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
        none
        """
        self.spb_dynamicMax = False
        self.setMaximumSize(width, height)
        self.spb_maximSize = (width, height)
        self.update()


    def spb_setNoProgressBar(self, num):
        """
        By default the Number of progress bar in spiralProgressBar is: 3,
        Users can increase the number of progress bar upto 6.(min: 2), this function
        is used to do exactly that.
        ...

        Parameters
        --------------
        num : int
            Number of progress bar.

        Raises
        --------------
        Exception : "Supported Format: int and not: " + type(num)
            raised when the user passes a non-int 'num' to the method.
        """
        if type(num)!=type(5):                            #MAKING SURE THAT THE ENTERED IS A NUMBER AND NOT A STRING OR OTHERS
            raise Exception("Supported Format: int and not: " + str(type(num)))
        if num<=6 and num>=2:
            self.noProgBar = num
            self.spb_value = []
            self.spb_maximValue = []
            self.spb_minimValue = []
            self.spb_startPos = []
            self.spb_direction = []
            self.lineColor = []
            self.lineStyle = []
            self.lineCap = []
            for each in range(0, self.noProgBar, 1):
                self.spb_value.append(-12*self.noProgBar*16/(each+1))
                self.spb_maximValue.append(100)
                self.spb_minimValue.append(0)
                self.spb_startPos.append(self.startPosFlags.North)
                self.spb_direction.append(self.rotationFlags.Clockwise)
                self.lineColor.append([0, 159, 227])
                self.lineStyle.append(self.lineStyleFlags.SolidLine)
                self.lineCap.append(self.lineCapFlags.RoundCap)
                self.pathColor.append([179, 241, 215])
                self.pathStyle.append(self.lineStyleFlags.SolidLine)
            self.update()


    def spb_setValue(self, value):                                 #value: TUPLE OF (value1, value2, value3)
        """
        Set the current value of the Progress Bar. maximum value >= Value >= minimum Value
        The user can set the value of each progress bar within the spiralprogressbar independely.
        The 'value' tuple element order corresponds to the outer to inner most progressbar.
        ...

        Parameters
        --------------
        value : tuple
            Ex: value = (0, 50, 22), this means value of outermost progress bar has the value of 0, 
            midden one to 50, and innermost to 22.

        Raises
        --------------
        Exception : "Value should be a tuple and not " + type(value)
            Rasied when the user passes a non-tuple data type to the module.

        ValueError : "Tuple length more than number of Progress Bars"
            Raised when the tuple contains more element than the number of concentric progress bar in the spiralProgressBar widget.

        ValueError : "Tuple length less than the number of Progress Bars"
            Raised when the tuple contains less element than the number of concentric progress bar in the spiralProgressBar widget.
        """

        if type(value)!=type(()):                                  #IF INPUT IS NOT A TUPLE
            raise Exception("Value should be a Tuple and not " + str(type(value)))
        elif len(value) > self.noProgBar:                        #IF TUPLE LENGTH IS MORE THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length more than number of Progress Bars")
        elif len(value) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length less than the number of Progress Bars")
        elif self.spb_value!=value:                                #IF EVERY THING GOES RIGHT
            for each in range(0, self.noProgBar, 1):
                if value[each]!='nc':                           #nc: NOC CHANGE STRING FOR ELEIMINATING THE NO CHANGE PROGRESS VALUES
                    if value[each] < self.spb_minimValue[each]:
                        spiralProgressBar.convValue(self, self.spb_minimValue[each], each)
                    elif value[each] > self.spb_maximValue[each]:
                        spiralProgressBar.convValue(self, self.spb_maximValue[each], each)
                    else:
                        spiralProgressBar.convValue(self, value[each], each)
            self.update()


    def spb_setMaximum(self, maxVal):
        """
        Maximum Value of the progressbar, default is 100.
        ...

        Parameters
        --------------
        maxVal : tuple
            Maximum value of each progressbar, in tuple, with elements in order 
            Ex: maxVal = (100, 200, 300) : corresponding to 100 for the outermost, 200
            for middle progress bar, 300 for innermost progressbar. 

        Raises
        --------------
        Exception : "The Max. for should be in form of a Tuple and not: " + type(maxVal)
            Rasied when the user passes a non-tuple data type to the module.

        ValueError : "Tuple length more than number of Progress Bars"
            Raised when the tuple contains more element than the number of concentric progress bar in the spiralProgressBar widget.

        ValueError : "Tuple length less than the number of Progress Bars"
            Raised when the tuple contains less element than the number of concentric progress bar in the spiralProgressBar widget.
        """

        if type(maxVal)!=type(()):                              #IF INPUT IS NOT A TUPLE
            raise Exception("The Max. for should be in form of a Tuple and not: " + str(type(maxVal)))
        elif len(maxVal) > self.noProgBar:                        #IF TUPLE LENGTH IS MORE THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length more than number of Progress Bars")
        elif len(maxVal) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length less than the number of Progress Bars")
        elif self.spb_maximValue!=maxVal:
            for each in range(0, self.noProgBar, 1):               #TO AVOID FUTURE DIVISION BY ZERO ERROR
                if maxVal[each]==self.spb_minimValue[each]:
                    raise ValueError("Maximum and Minimum Value Cannot be the Same")
            self.spb_maximValue = list(maxVal)
            self.update()


    def spb_setMinimum(self, minVal):
        """
        Minimum Value of the progressbar, default is 0.
        ...

        Parameters
        --------------
        minVal : tuple
            Minimum value of each progressbar, in tuple, with elements in order 
            Ex: minVal = (0, 10, 20) : corresponding to 0 for the outermost, 10
            for middle progress bar, 20 for innermost progressbar. 

        Raises
        --------------
        Exception : "The Min. for should be in form of a Tuple and not: " + type(minVal)
            Rasied when the user passes a non-tuple data type to the module.

        ValueError : "Tuple length more than number of Progress Bars"
            Raised when the tuple contains more element than the number of concentric progress bar in the spiralProgressBar widget.

        ValueError : "Tuple length less than the number of Progress Bars"
            Raised when the tuple contains less element than the number of concentric progress bar in the spiralProgressBar widget.
        """

        if type(minVal)!=type(()):                              #IF INPUT IS NOT A TUPLE
            raise Exception("The Min. for should be in form of a Tuple and not: " + str(type(minVal)))
        elif len(minVal) > self.noProgBar:                        #IF TUPLE LENGTH IS MORE THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length more than number of Progress Bars")
        elif len(minVal) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length less than the number of Progress Bars")
        elif self.spb_minimValue!=minVal:
            for each in range(0, self.noProgBar, 1):               #TO AVOID FUTURE DIVISION BY ZERO ERROR
                if minVal[each]==self.spb_maximValue[each]:
                    raise ValueError("Maximum and Minimum Value Cannot be the Same")
            self.spb_minimValue = list(minVal)
            self.update()


    def spb_setRange(self, minTuple, maxTuple):
        """
        This function does the job of setting the Maximum value and Minimum value in one go.
        ...

        Parameters
        --------------
        maxTuple : tuple
            Maximum value of each progressbar, in tuple, with elements in order 
            Ex: maxVal = (100, 200, 300) : corresponding to 100 for the outermost, 200
            for middle progress bar, 300 for innermost progressbar. 

        minVal : tuple
            Minimum value of each progressbar, in tuple, with elements in order 
            Ex: minVal = (0, 10, 20) : corresponding to 0 for the outermost, 10
            for middle progress bar, 20 for innermost progressbar. 

        Raises
        --------------
        Exception : "The Minimum and Maximum should be a Tuple"
            Rasied when the user passes a non-tuple data type to the module.

        ValueError : "Tuple length more than number of Progress Bars"
            Raised when the tuple contains more element than the number of concentric progress bar in the spiralProgressBar widget.

        ValueError : "Tuple length less than the number of Progress Bars"
            Raised when the tuple contains less element than the number of concentric progress bar in the spiralProgressBar widget.
        """

        if type(minTuple)!=type(()) or type(maxTuple)!=type(()):
            raise Exception("The Minimum and Maximum should be a Tuple")
        elif len(minTuple) > self.noProgBar or len(maxTuple) > self.noProgBar:
            raise ValueError("Minimum/Maximum Tuple length exceeds the number of Progress Bar")
        elif len(minTuple) < self.noProgBar or len(maxTuple) < self.noProgBar:
            raise ValueError("Minimum/Maximum Tuple length is less than the number of Progress Bar")
        for each in range(0, self.noProgBar, 1):
            if minTuple[each]==maxTuple[each]:
                raise ValueError("Minimum and Maximum cannot be the Same")
        self.spb_minimValue = minTuple
        self.spb_maximValue = maxTuple
        self.update()


    def spb_setGap(self, gap):
        """
        Set the Gap between each concentric circle in the spiralProgressBar.
        Default is : gap = 2*line width
        ...

        Parameters
        --------------
        gap : int
        Try different settings by passing an int to the function: 'int' corresponds to the "px" seperation
        between the concentric circles.  

        Raises
        --------------
        Exception : "Gap should be an integer and not: " + type(gap)
            Rasied when the user passes a non-tuple data type to the module.
        """

        if type(gap)!=type(5):
            raise ValueError("Gap should be an integer and not: " + str(type(gap)))
        else:
            self.spb_gap = gap
            self.gapCngd = True
            self.update()


    def spb_setInitialPos(self, position):
        """
        Sets the statring point of the progress bar or the 0% position.
        Default is 'North'
        ...

        Parameters
        --------------
        position : tuple
            The tuple elements accepts only string of : 'North', 'South', 'East' and 'West'.
            The order of arrangment matters i.e. the first element corresponds to the outer most concentric 
            progress bar and the last element correspinds to the innermost circle. 
            Ex : position = ('North', 'South', 'East')

        Raises
        --------------
        Exception : "Position should be a Tuple and not " + type(position)
            Rasied when the user passes a non-tuple data type to the module.

        ValueError : "Tuple length more than number of Progress Bars"
            Raised when the tuple contains more element than the number of concentric progress bar in the spiralProgressBar widget.

        ValueError : "Tuple length less than the number of Progress Bars"
            Raised when the tuple contains less element than the number of concentric progress bar in the spiralProgressBar widget.
        """

        if type(position)!=type(()):                                  #IF INPUT IS NOT A TUPLE
            raise Exception("Position should be a Tuple and not " + str(type(position)))
        elif len(position) > self.noProgBar:                        #IF TUPLE LENGTH IS MORE THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length more than number of Progress Bars")
        elif len(position) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length less than the number of Progress Bars")
        else:
            for each in range(0, self.noProgBar, 1):
                if type(position[each])!=type("string"):
                    raise Exception("Position Tuple elements should be String and not: " + str(type(position[each])))
                elif position[each]=='North':
                    self.spb_startPos[each] = self.startPosFlags.North
                elif position[each]=='South':
                    self.spb_startPos[each] = self.startPosFlags.South
                elif position[each]=='East':
                    self.spb_startPos[each] = self.startPosFlags.East
                elif position[each]=='West':
                    self.spb_startPos[each] = self.startPosFlags.West
                else:
                    raise Exception("Position can hold Property: 'North', 'South', 'East' and 'West' and not: " + position[each])
            self.update()


    def spb_reset(self):
        """
        Resets the progress bar to the 0%.
        ...

        Parameters
        --------------
        none

        Raises
        --------------
        none
        """

        for each in range(0, self.noProgBar, 1):
            spiralProgressBar.convValue(self, self.spb_minimValue[each], each)
        self.update()


    def spb_setGeometry(self, posX, posY):
        """
        This module changes the position of the widget. Default it is : (0, 0).
        ...

        Parameters
        --------------
        posX : int
            The vertical position of the widget from the top of the window inside which the widget lies.
            By default it is 0. The user can change the position to better suite his style and positioning of the
            widget.

        posY : int

        Raises
        --------------
        Exception : Position should be an int
            If the user passes a non-int data type.
        """ 

        if type(posX)!=type(5) or type(posY)!=type(5):
            raise Exception("Position should be a int and not: X" + str(type(posX))) + ", Y: " + str(type(posY))
            return
        if self.positionX!=posX:
            self.positionX = posX
        if self.positionY!=posY:
            self.positionY = posY
        self.update()


    def spb_setDirection(self, direction):
        """
        Direction of rotation of the spiral progress bar.
        ...

        Parameters
        --------------
        direction : tuple
            Direction that the round progress bar can hold are : 'Clockwise' and 'AntiClockwise'
            Default is 'Clockwise'. The tuple take string as elements corresponding to the direction of
            each of the concentric circles.

        Raises
        --------------
        Exception : "Direction should be a Tuple"
            Rasied when the user passes a non-tuple data type to the module.

        ValueError : "Tuple length more than number of Progress Bars"
            Raised when the tuple contains more element than the number of concentric progress bar in the spiralProgressBar widget.

        ValueError : "Tuple length less than the number of Progress Bars"
            Raised when the tuple contains less element than the number of concentric progress bar in the spiralProgressBar widget.

        Exception : "Direction Tuple elements should be String"
            Rasies when the elements of the tuple is not a string.
        """

        if type(direction)!=type(()):                                  #IF INPUT IS NOT A TUPLE
            raise Exception("Direction should be a Tuple and not " + str(type(direction)))
        elif len(direction) > self.noProgBar:                        #IF TUPLE LENGTH IS MORE THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length more than number of Progress Bars")
        elif len(direction) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length less than the number of Progress Bars")
        else:
            for each in range(0, self.noProgBar, 1):
                if type(direction[each])!=type("String"):
                    raise Exception("Direction Tuple elements should be String and not: " + str(type(direction[each])))
                elif direction[each]=='Clockwise':
                    self.spb_direction[each] = self.rotationFlags.Clockwise
                elif direction[each]=='AntiClockwise':
                    self.spb_direction[each] = self.rotationFlags.AntiClockwise
                else:
                    raise Exception("Direction can hold Property: 'Clockwise'/'AntiClockwise' and not: " + str(type(direction[each])))
            self.update()


    def variableWidth(self, inp):
        """
        A flag for varing the progress bar size.
        ...

        Parameters
        --------------
        inp : bool
            True : Changes the size of the width of line progressely.

        Raises
        --------------
        Exception : Variable width should be a bool : True/False
            Rasied when the user passes a non-bool data type to the module.
        """

        if type(inp)!=type(True):
            raise Exception("Variable Width should be a Bool and not " + str(type(inp)))
        else:
            self.varWidth = inp
            self.update()


    def spb_widthIncrement(self, increm):
        """
        Width increment for incrment in the line width. Default is 1px. User can sepcify the
        amount of px to increment form the outer to inner circle progressbar.
        ...

        Parameters
        --------------
        incrment : int
            Increment passed to the module as int px.

        Raises
        --------------
        Exception : Increment should be an integer
            Rasied when the user passes a non-int data type to the module.
        """

        if type(increm)!=type(5):
            raise Exception("Increment should be an integer and not " + str(type(increm)))
        else:
            self.widthIncr = increm
            self.update()


    def spb_lineWidth(self, width):
        """
        Line width of the circles in the spiral progress bar.
        ...

        Parameters
        --------------
        width : int

        Raises
        --------------
        Exception : Width should be an Integer
            Rasied when the user passes a non-int data type to the module.
        """

        if type(width)!=type(5):
            raise Exception("Width should be an Integer and not " + str(type(width)))
        else:
            self.lineWidth = width
            if self.gapCngd!=True:
                self.spb_gap = self.lineWidth*2
            self.update()


    def spb_lineColor(self, color):
        """
        Color of line in the spiral progress bar. Each concentric progress bar has its own color settings. 
        ...

        Parameters
        --------------
        color : tuple
            Color tuple corresponds to the color of each line which is a tuple of (R, G, B).
            Ex : color = ((R, G, B), (R, G, B), (R, G, B))
            Elements of the color tuple is in correspondance with the order : outer to innermost circles in progress bar.

        Raises
        --------------
        Exception : Color should be a Tuple
            Rasied when the user passes a non-tuple data type to the module.

        ValueError : "Tuple length more than number of Progress Bars"
            Raised when the tuple contains more element than the number of concentric progress bar in the spiralProgressBar widget.

        ValueError : "Tuple length less than the number of Progress Bars"
            Raised when the tuple contains less element than the number of concentric progress bar in the spiralProgressBar widget.
        """

        if type(color)!=type(()):
            raise Exception("Color should be a Tuple and not " + str(type(Color)))
        elif type(color[0])!=type(()):
            raise Exception("Color should be in Format: ((R, G, B), (R, G, B), (R, G, B)) and not any other")
        elif len(color) > self.noProgBar:
            raise ValueError("Tuple length more than number of Progress Bars")
        elif len(color) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length less than the number of Progress Bars")
        else:
            for each in range(0, self.noProgBar, 1):
                if len(color[each])!=3:
                    raise Exception('Color should be in format (R, G, B)')
                elif self.lineColor[each]!=color[each]:
                    self.lineColor[each] = color[each]
            self.update()


    def spb_lineStyle(self, style):
        """
        line style of the spiral progress bar.
        ...

        Parameters
        --------------
        style : tuple
            Style types : 'SolidLine', 'DotLine' and 'DashLine'.
            Users can pass the style for each progress bar in the order : first element corresponds 
            to the styleof outermost progressbar and viceversa.

        Raises
        --------------
        Exception : Style should be a tuple
            Rasied when the user passes a non-tuple data type to the module.

        ValueError : "Tuple length more than number of Progress Bars"
            Raised when the tuple contains more element than the number of concentric progress bar in the spiralProgressBar widget.

        ValueError : "Tuple length less than the number of Progress Bars"
            Raised when the tuple contains less element than the number of concentric progress bar in the spiralProgressBar widget.
        """

        if type(style)!=type(()):
            raise Exception("Style should be a tuple and not: " + str(type(style)))
        elif len(style) > self.noProgBar:                        #IF TUPLE LENGTH IS MORE THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length more than number of Progress Bars")
        elif len(style) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length less than the number of Progress Bars")
        else:
            for each in range(0, self.noProgBar, 1):
                if type(style[each])!=type("String"):
                    raise Exception("Style Tuple element should be a String and not: " + str(type(style[each])))
                elif style[each]=='SolidLine':
                    self.lineStyle[each] = self.lineStyleFlags.SolidLine
                elif style[each]=='DotLine':
                    self.lineStyle[each] = self.lineStyleFlags.DotLine
                elif style[each]=='DashLine':
                    self.lineStyle[each] = self.lineStyleFlags.DashLine
                else:
                    raise Exception("Style can hold 'SolidLine', DotLine' and 'DashLine' only.")
            self.update()


    def spb_lineCap(self, cap):
        """
        Cap i.e. the end of the line : to be Round or Square.
        ...

        Parameters
        --------------
        cap : tuple
            Cap : 'RoundCap' and 'SquareCap'.
            Users can pass the desired cap of the line as a string passed in the following order of : 
            Outer progress bar : first element in the tuple and viceversa.

        Raises
        --------------
        Exception : Cap should be a tuple
            Rasied when the user passes a non-tuple data type to the module.

        ValueError : "Tuple length more than number of Progress Bars"
            Raised when the tuple contains more element than the number of concentric progress bar in the spiralProgressBar widget.

        ValueError : "Tuple length less than the number of Progress Bars"
            Raised when the tuple contains less element than the number of concentric progress bar in the spiralProgressBar widget.
        """
        
        if type(cap)!=type(()):
            raise Exception("Cap should be a tuple and not: " + str(type(cap)))
        elif len(cap) > self.noProgBar:                        #IF TUPLE LENGTH IS MORE THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length more than number of Progress Bars")
        elif len(cap) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length less than the number of Progress Bars")
        else:
            for each in range(0, self.noProgBar, 1):
                if type(cap[each])!=type("String"):
                    raise Exception('Cap Tuple element should be a String and not a: ' + str(type(cap[each])))
                elif cap[each]=='SquareCap':
                    self.lineCap[each] = self.lineCapFlags.SquareCap
                elif cap[each]=='RoundCap':
                    self.lineCap[each] = self.lineCapFlags.RoundCap
                else:
                    raise Exception("Cap can hold 'SquareCap' and 'RoundCap' only")
            self.update()


    def spb_setPathHidden(self, hide):
        """
        Hides the path in the spiral progress bar.
        ...

        Parameters
        --------------
        hide : bool

        Raises
        --------------
        Exception : Hidden accept a bool
            Rasied when the user passes a non-bool data type to the module.
        """

        if type(hide)!=type(True):
            raise Exception("Hidden accept a bool and not: " + str(type(hide)))
        elif hide==True:
            self.pathPresent = False
        else:
            self.pathPresent = True

    def spb_pathColor(self, color):
        """
        Color of path in the spiral progress bar. Each concentric progress bar has its own color settings. 
        ...

        Parameters
        --------------
        color : tuple
            Color tuple corresponds to the color of each path which is a tuple of (R, G, B).
            Ex : color = ((R, G, B), (R, G, B), (R, G, B))
            Elements of the color tuple is in correspondance with the order : outer to innermost circles in progress bar.

        Raises
        --------------
        Exception : Color should be a Tuple
            Rasied when the user passes a non-tuple data type to the module.

        ValueError : "Tuple length more than number of Progress Bars"
            Raised when the tuple contains more element than the number of concentric progress bar in the spiralProgressBar widget.

        ValueError : "Tuple length less than the number of Progress Bars"
            Raised when the tuple contains less element than the number of concentric progress bar in the spiralProgressBar widget.
        """

        if type(color)!=type(()):
            raise Exception("Color should be a Tuple and not " + str(type(Color)))
        elif type(color[0])!=type(()):
            raise Exception("Color should be in Format: ((R, G, B), (R, G, B), (R, G, B)) and not any other")
        elif len(color) > self.noProgBar:
            raise ValueError("Tuple length more than number of Progress Bars")
        elif len(color) < self.noProgBar:                        #IF INPUT TUPLE LENGTH IS LESS THAN THE NUMBER OF PROGRESS BAR
            raise ValueError("Tuple length less than the number of Progress Bars")
        else:
            for each in range(0, self.noProgBar, 1):
                if len(color[each])!=3:
                    raise Exception('Color should be in format (R, G, B)')
                elif self.pathColor[each]!=color[each]:
                    self.pathColor[each] = color[each]
            self.update()


#------------------------------------------------------METHODS FOR GETTING THE PROPERTY OF SPIRALPROGRESSBAR SLOTS

#------------------------------------------------------ENGINE: WHERE ALL THE REAL STUFF TAKE PLACE: WORKING OF THE SPIRALPROGRESSBAR


    def spb_MinimumSize(self, dynMax, minim, maxim):
        """
        Realtime automatic minimum size determiner for the spiral progress bar.
        For this to achieve the function first checks the size of the layout, where the spiralprogressbar lies.
        From that info the, it calculate the minimum size for the spiral progressbar so that all the circles in the spiral
        progress bar is clearly visible.
        
        ...
        Parameters
        --------------
        none.

        Return
        --------------
        none.
        """

        spb_Height = self.height()
        spb_Width = self.width()

        if dynMax:
            if spb_Width >= spb_Height and spb_Height >= minim[1]:
                self.spb_Size = spb_Height
            elif spb_Width < spb_Height and spb_Width >= minim[0]:
                self.spb_Size = spb_Width
        else:
            if spb_Width >= spb_Height and spb_Height <= maxim[1]:
                self.spb_Size = spb_Height
            elif spb_Width < spb_Height and spb_Width <= maxim[0]:
                self.spb_Size = spb_Width


    def geometricFactor(self):
        """
        Width of the line should be subrtracted from the size of the progrress bar, inorder to properly 
        fit inot the layout properly without any cut in the widget margins.
        
        ...
        Parameters
        --------------
        none.

        Return
        --------------
        none.
        """
        self.posFactor = self.lineWidth/2 + 1
        self.sizeFactor = self.lineWidth + 1


    def convValue(self, value, pos):
        """
        Convert the value from the user entered to the percentage depending on the maximum and minimum value.
        Calculagted by the relation : (value - minimum)/(maximum - minimum)
        
        ...
        Parameters
        --------------
        none.

        Return
        --------------
        none.
        """

        self.spb_value[pos] = ((value - self.spb_minimValue[pos])/(self.spb_maximValue[pos] - self.spb_minimValue[pos]))*360*16
        self.spb_value[pos] = self.spb_direction[pos]*self.spb_value[pos]



    def paintEvent(self, event: QPaintEvent):
        """
        The place where the drawing takes palce.
        
        ...
        Parameters
        --------------
        none.

        Return
        --------------
        none.
        """

        if self.spb_dynamicMin:
            self.setMinimumSize(QSize(self.lineWidth*6 + self.pathWidth*6, self.lineWidth*6 + self.pathWidth*6))

        spiralProgressBar.spb_MinimumSize(self, self.spb_dynamicMax, self.spb_minimSize, self.spb_maximSize)
        spiralProgressBar.geometricFactor(self)
        spiralIncrem = 0
        spiralIncrem2 = 0


        if self.pathIndepend!=True:
            self.pathWidth = self.lineWidth
        self.tempWidth = self.pathWidth
        if self.pathPresent:
            for path in range(0, self.noProgBar, 1):
                if self.varWidth==True:   #CREAETS A INCREASING OR DECREASING TYPE OF WITH 
                    self.tempWidth = self.tempWidth + self.widthIncr
                    if self.gapCngd!=True:
                        self.spb_gap = self.tempWidth*2
                self.pathPainter = QPainter(self)
                self.pathPainter.setRenderHint(QPainter.Antialiasing)
                self.penPath = QPen()
                self.penPath.setStyle(self.pathStyle[path])
                self.penPath.setWidth(self.tempWidth)
                self.penPath.setBrush(QColor(self.pathColor[path][0], self.pathColor[path][1], self.pathColor[path][2]))
                self.pathPainter.setPen(self.penPath)
                self.pathPainter.drawArc(self.positionX + self.posFactor + self.spb_cngSize*spiralIncrem2, self.positionY + self.posFactor + self.spb_cngSize*spiralIncrem2, self.spb_Size - self.sizeFactor - 2*self.spb_cngSize*spiralIncrem2, self.spb_Size - self.sizeFactor - 2*self.spb_cngSize*spiralIncrem2, self.spb_startPos[path], 360*16)
                self.pathPainter.end()
                spiralIncrem2 = spiralIncrem2 + self.spb_gap
                

        self.tempWidth = self.lineWidth   #TEMPWIDTH TEMPORARLY STORES THE LINEWIDTH, USEFUL IN VARIABLE WIDTH OPTION.
        for bar in range(0, self.noProgBar, 1):
            if self.varWidth==True:   #CREAETS A INCREASING OR DECREASING TYPE OF WITH 
                self.tempWidth = self.tempWidth + self.widthIncr
                if self.gapCngd!=True:
                    self.spb_gap = self.tempWidth*2
            self.linePainter = QPainter(self)
            self.linePainter.setRenderHint(QPainter.Antialiasing)
            self.penLine = QPen()
            self.penLine.setStyle(self.lineStyle[bar])
            self.penLine.setWidth(self.tempWidth)
            self.penLine.setCapStyle(self.lineCap[bar])
            self.penLine.setBrush(QColor(self.lineColor[bar][0], self.lineColor[bar][1], self.lineColor[bar][2]))
            self.linePainter.setPen(self.penLine)
            self.linePainter.drawArc(self.positionX + self.posFactor + self.spb_cngSize*spiralIncrem, self.positionY + self.posFactor + self.spb_cngSize*spiralIncrem, self.spb_Size - self.sizeFactor - 2*self.spb_cngSize*spiralIncrem, self.spb_Size - self.sizeFactor - 2*self.spb_cngSize*spiralIncrem, self.spb_startPos[bar], self.spb_value[bar])
            self.linePainter.end()
            spiralIncrem = spiralIncrem + self.spb_gap


#------------------------------------------------------

if __name__=="__main__":
    print("Try Import.")