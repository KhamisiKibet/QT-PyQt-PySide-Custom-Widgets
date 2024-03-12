from qtpy.QtCore import *
from qtpy import QtCore
########################################################################
##
########################################################################
def returnAnimationEasingCurve(easingCurveName):
    if len(str(easingCurveName)) > 0:
        if str(easingCurveName) == "OutQuad":
            return QtCore.QEasingCurve.OutQuad
        elif str(easingCurveName) == "Linear":
            return QtCore.QEasingCurve.Linear
        elif str(easingCurveName) == "InQuad":
            return QtCore.QEasingCurve.InQuad
        elif str(easingCurveName) == "InOutQuad":
            return QtCore.QEasingCurve.InOutQuad
        elif str(easingCurveName) == "OutInQuad":
            return QtCore.QEasingCurve.OutInQuad
        elif str(easingCurveName) == "InCubic":
            return QtCore.QEasingCurve.InCubic
        elif str(easingCurveName) == "OutCubic":
            return QtCore.QEasingCurve.OutCubic
        elif str(easingCurveName) == "InOutCubic":
            return QtCore.QEasingCurve.InOutCubic
        elif str(easingCurveName) == "OutInCubic":
            return QtCore.QEasingCurve.OutInCubic
        elif str(easingCurveName) == "InQuart":
            return QtCore.QEasingCurve.InQuart
        elif str(easingCurveName) == "OutQuart":
            return QtCore.QEasingCurve.OutQuart
        elif str(easingCurveName) == "InOutQuart":
            return QtCore.QEasingCurve.InOutQuart
        elif str(easingCurveName) == "OutInQuart":
            return QtCore.QEasingCurve.OutInQuart
        elif str(easingCurveName) == "InQuint":
            return QtCore.QEasingCurve.InQuint
        elif str(easingCurveName) == "OutQuint":
            return QtCore.QEasingCurve.OutQuint
        elif str(easingCurveName) == "InOutQuint":
            return QtCore.QEasingCurve.InOutQuint
        elif str(easingCurveName) == "InSine":
            return QtCore.QEasingCurve.InSine
        elif str(easingCurveName) == "OutSine":
            return QtCore.QEasingCurve.OutSine
        elif str(easingCurveName) == "InOutSine":
            return QtCore.QEasingCurve.InOutSine
        elif str(easingCurveName) == "OutInSine":
            return QtCore.QEasingCurve.OutInSine
        elif str(easingCurveName) == "InExpo":
            return QtCore.QEasingCurve.InExpo
        elif str(easingCurveName) == "OutExpo":
            return QtCore.QEasingCurve.OutExpo
        elif str(easingCurveName) == "InOutExpo":
            return QtCore.QEasingCurve.InOutExpo
        elif str(easingCurveName) == "OutInExpo":
            return QtCore.QEasingCurve.OutInExpo
        elif str(easingCurveName) == "InCirc":
            return QtCore.QEasingCurve.InCirc
        elif str(easingCurveName) == "OutCirc":
            return QtCore.QEasingCurve.OutCirc
        elif str(easingCurveName) == "InOutCirc":
            return QtCore.QEasingCurve.InOutCirc
        elif str(easingCurveName) == "OutInCirc":
            return QtCore.QEasingCurve.OutInCirc
        elif str(easingCurveName) == "InElastic":
            return QtCore.QEasingCurve.InElastic
        elif str(easingCurveName) == "OutElastic":
            return QtCore.QEasingCurve.OutElastic
        elif str(easingCurveName) == "InOutElastic":
            return QtCore.QEasingCurve.InOutElastic
        elif str(easingCurveName) == "OutInElastic":
            return QtCore.QEasingCurve.OutInElastic
        elif str(easingCurveName) == "InBack":
            return QtCore.QEasingCurve.InBack
        elif str(easingCurveName) == "OutBack":
            return QtCore.QEasingCurve.OutBack
        elif str(easingCurveName) == "InOutBack":
            return QtCore.QEasingCurve.InOutBack
        elif str(easingCurveName) == "OutInBack":
            return QtCore.QEasingCurve.OutInBack
        elif str(easingCurveName) == "InBounce":
            return QtCore.QEasingCurve.InBounce
        elif str(easingCurveName) == "OutBounce":
            return QtCore.QEasingCurve.OutBounce
        elif str(easingCurveName) == "InOutBounce":
            return QtCore.QEasingCurve.InOutBounce
        elif str(easingCurveName) == "OutInBounce":
            return QtCore.QEasingCurve.OutInBounce
        else:
            raise Exception("Unknown value'" +easingCurveName+ "' for setEasingCurve()")
########################################################################
##
########################################################################

########################################################################
##
########################################################################
def returnQtDirection(direction):
    if len(str(direction)) > 0:
        if str(direction) == "horizontal":
            return QtCore.Qt.Horizontal
        elif str(direction) == "vertical":
            return QtCore.Qt.Vertical
        else:
            raise Exception("Unknown direction name given ("+direction+"), please use Vertical or Horizontal direction")

    else:
        raise Exception("Empty direction name given, please use Vertical or Horizontal direction")