from qtpy.QtCore import QEasingCurve, Qt
########################################################################
##
########################################################################
def returnAnimationEasingCurve(easingCurveName):
    if len(str(easingCurveName)) > 0:
        if str(easingCurveName) == "OutQuad":
            return QEasingCurve.OutQuad
        elif str(easingCurveName) == "Linear":
            return QEasingCurve.Linear
        elif str(easingCurveName) == "InQuad":
            return QEasingCurve.InQuad
        elif str(easingCurveName) == "InOutQuad":
            return QEasingCurve.InOutQuad
        elif str(easingCurveName) == "OutInQuad":
            return QEasingCurve.OutInQuad
        elif str(easingCurveName) == "InCubic":
            return QEasingCurve.InCubic
        elif str(easingCurveName) == "OutCubic":
            return QEasingCurve.OutCubic
        elif str(easingCurveName) == "InOutCubic":
            return QEasingCurve.InOutCubic
        elif str(easingCurveName) == "OutInCubic":
            return QEasingCurve.OutInCubic
        elif str(easingCurveName) == "InQuart":
            return QEasingCurve.InQuart
        elif str(easingCurveName) == "OutQuart":
            return QEasingCurve.OutQuart
        elif str(easingCurveName) == "InOutQuart":
            return QEasingCurve.InOutQuart
        elif str(easingCurveName) == "OutInQuart":
            return QEasingCurve.OutInQuart
        elif str(easingCurveName) == "InQuint":
            return QEasingCurve.InQuint
        elif str(easingCurveName) == "OutQuint":
            return QEasingCurve.OutQuint
        elif str(easingCurveName) == "InOutQuint":
            return QEasingCurve.InOutQuint
        elif str(easingCurveName) == "InSine":
            return QEasingCurve.InSine
        elif str(easingCurveName) == "OutSine":
            return QEasingCurve.OutSine
        elif str(easingCurveName) == "InOutSine":
            return QEasingCurve.InOutSine
        elif str(easingCurveName) == "OutInSine":
            return QEasingCurve.OutInSine
        elif str(easingCurveName) == "InExpo":
            return QEasingCurve.InExpo
        elif str(easingCurveName) == "OutExpo":
            return QEasingCurve.OutExpo
        elif str(easingCurveName) == "InOutExpo":
            return QEasingCurve.InOutExpo
        elif str(easingCurveName) == "OutInExpo":
            return QEasingCurve.OutInExpo
        elif str(easingCurveName) == "InCirc":
            return QEasingCurve.InCirc
        elif str(easingCurveName) == "OutCirc":
            return QEasingCurve.OutCirc
        elif str(easingCurveName) == "InOutCirc":
            return QEasingCurve.InOutCirc
        elif str(easingCurveName) == "OutInCirc":
            return QEasingCurve.OutInCirc
        elif str(easingCurveName) == "InElastic":
            return QEasingCurve.InElastic
        elif str(easingCurveName) == "OutElastic":
            return QEasingCurve.OutElastic
        elif str(easingCurveName) == "InOutElastic":
            return QEasingCurve.InOutElastic
        elif str(easingCurveName) == "OutInElastic":
            return QEasingCurve.OutInElastic
        elif str(easingCurveName) == "InBack":
            return QEasingCurve.InBack
        elif str(easingCurveName) == "OutBack":
            return QEasingCurve.OutBack
        elif str(easingCurveName) == "InOutBack":
            return QEasingCurve.InOutBack
        elif str(easingCurveName) == "OutInBack":
            return QEasingCurve.OutInBack
        elif str(easingCurveName) == "InBounce":
            return QEasingCurve.InBounce
        elif str(easingCurveName) == "OutBounce":
            return QEasingCurve.OutBounce
        elif str(easingCurveName) == "InOutBounce":
            return QEasingCurve.InOutBounce
        elif str(easingCurveName) == "OutInBounce":
            return QEasingCurve.OutInBounce
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
            return Qt.Horizontal
        elif str(direction) == "vertical":
            return Qt.Vertical
        else:
            raise Exception("Unknown direction name given ("+direction+"), please use Vertical or Horizontal direction")

    else:
        raise Exception("Empty direction name given, please use Vertical or Horizontal direction")