#####
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinncode.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys

from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtGui import QFontDatabase


################################################################################################
# Import the generated UI
################################################################################################
from ui_interface import *

################################################################################################
# MAIN WINDOW CLASS
################################################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        ################################################################################################
        # Setup the UI main window
        ################################################################################################
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ################################################################################################
        # Show window
        ################################################################################################
        self.show()

        ################################################################################################
        # CUSTOMIZE ANALOGUE GAUGE WIDGET
        ################################################################################################
        self.ui.widget.enableBarGraph = True

        self.ui.widget.valueNeedleSnapzone = 1

        ################################################################################################
        # Set gauge units
        ################################################################################################
        self.ui.widget.units = "Km/h"

        ################################################################################################
        # Set minimum gauge value
        ################################################################################################
        self.ui.widget.minValue = 0
        ################################################################################################
        # Set maximum gauge value
        ################################################################################################
        self.ui.widget.maxValue = 100

        ################################################################################################
        # Set scale divisions
        ################################################################################################
        self.ui.widget.scalaCount = 10

        # Start from the minimum value
        # self.ui.widget.updateValue(self.ui.widget.minValue)
        # OR
        # Start from half/middle value
        self.ui.widget.updateValue(int(self.ui.widget.maxValue - self.ui.widget.minValue)/2)


        ################################################################################################
        # Set slider minimum and maximum value
        ################################################################################################
        self.ui.ActualValueSlider.setMaximum(self.ui.widget.maxValue)
        self.ui.ActualValueSlider.setMinimum(self.ui.widget.minValue)
        self.ui.ActualValueSlider.setValue(self.ui.widget.value)

        ################################################################################################
        # Set slider gauge outer radius
        ################################################################################################
        self.ui.OuterRadiusSlider.setValue(self.ui.widget.gauge_color_outer_radius_factor * 1000)
        self.ui.lcdOuterRadius.display(self.ui.widget.gauge_color_outer_radius_factor * 1000)

        ################################################################################################
        # Set slider gauge inner radius
        ################################################################################################
        self.ui.InnenRadiusSlider.setValue(int(self.ui.widget.gauge_color_inner_radius_factor) * 1000)
        self.ui.lcdInnerRadius.display(self.ui.widget.gauge_color_inner_radius_factor * 1000)

        ################################################################################################
        # Set slider gauge start position
        ################################################################################################
        self.ui.GaugeStartSlider.setValue(self.ui.widget.scale_angle_start_value)
        self.ui.lcdGaugeStart.display(self.ui.widget.scale_angle_start_value)

        ################################################################################################
        # Set slider gauge size
        ################################################################################################
        self.ui.GaugeSizeSlider.setValue(self.ui.widget.scale_angle_size)
        self.ui.lcdGaugeSize.display(self.ui.widget.scale_angle_size)

        ################################################################################################
        # Set gauge start position
        ################################################################################################

        ################################################################################################
        # R G B A gauge needle color sliders
        ################################################################################################
        self.ui.RedSlider_Needle.valueChanged.connect(self.setNeedleColor)
        self.ui.GreenSlider_Needle.valueChanged.connect(self.setNeedleColor)
        self.ui.BlueSlider_Needle.valueChanged.connect(self.setNeedleColor)

        ################################################################################################
        # Transparency(A) gauge needle color sliders
        ################################################################################################
        self.ui.TrancSlider_Needle.valueChanged.connect(self.setNeedleColor)

        ################################################################################################
        # Update LCD RGBA needle color indicators
        ################################################################################################
        self.ui.lcdNumber_Red_Needle.display(self.ui.RedSlider_Needle.value())
        self.ui.lcdNumber_Green_Needle.display(self.ui.GreenSlider_Needle.value())
        self.ui.lcdNumber_Blue_Needle.display(self.ui.RedSlider_Needle.value())
        self.ui.lcdNumber_Trancparency_Needle.display(self.ui.TrancSlider_Needle.value())

        ################################################################################################
        # Update RGBA needle color indicators on user drag
        ################################################################################################
        self.ui.RedSlider_NeedleDrag.valueChanged.connect(self.setNeedleColorOnDrag)
        self.ui.GreenSlider_NeedleDrag.valueChanged.connect(self.setNeedleColorOnDrag)
        self.ui.BlueSlider_NeedleDrag.valueChanged.connect(self.setNeedleColorOnDrag)
        self.ui.TrancSlider_NeedleDrag.valueChanged.connect(self.setNeedleColorOnDrag)

        ################################################################################################
        # Update LCD RGBA needle color indicators on user drag
        ################################################################################################
        self.ui.lcdNumber_Red_NeedleDrag.display(self.ui.RedSlider_NeedleDrag.value())
        self.ui.lcdNumber_Green_NeedleDrag.display(self.ui.GreenSlider_NeedleDrag.value())
        self.ui.lcdNumber_Blue_NeedleDrag.display(self.ui.BlueSlider_NeedleDrag.value())
        self.ui.lcdNumber_Trancparency_NeedleDrag.display(self.ui.TrancSlider_NeedleDrag.value())


        ################################################################################################
        # Update RGBA scale text color
        ################################################################################################
        self.ui.RedSlider_Scale.valueChanged.connect(self.setScaleValueColor)
        self.ui.GreenSlider_Scale.valueChanged.connect(self.setScaleValueColor)
        self.ui.BlueSlider_Scale.valueChanged.connect(self.setScaleValueColor)
        self.ui.TrancSlider_Scale.valueChanged.connect(self.setScaleValueColor)

        ################################################################################################
        # Update RGBA LCD scale text color indicators
        ################################################################################################
        self.ui.lcdNumber_Red_Scale.display(self.ui.RedSlider_Scale.value())
        self.ui.lcdNumber_Green_Scale.display(self.ui.GreenSlider_Scale.value())
        self.ui.lcdNumber_Blue_Scale.display(self.ui.BlueSlider_Scale.value())
        self.ui.lcdNumber_Trancparency_Scale.display(self.ui.TrancSlider_Scale.value())


        ################################################################################################
        # Update RGBA value text color
        ################################################################################################
        self.ui.RedSlider_Display.valueChanged.connect(self.setDisplayValueColor)
        self.ui.GreenSlider_Display.valueChanged.connect(self.setDisplayValueColor)
        self.ui.BlueSlider_Display.valueChanged.connect(self.setDisplayValueColor)
        self.ui.TrancSlider_Display.valueChanged.connect(self.setDisplayValueColor)

        ################################################################################################
        # Update slider value
        ################################################################################################
        self.ui.ActualValueSlider.valueChanged.connect( lambda:  self.updateGaugeValue())
        self.ui.widget.valueChanged.connect( lambda:  self.updateSliderValue())

        self.ui.GaugeSizeSlider.valueChanged.connect( lambda:  self.updateScaleAngleSize())

        self.ui.GaugeStartSlider.valueChanged.connect( lambda:  self.updateStartScaleAngle())

        self.ui.InnenRadiusSlider.valueChanged.connect( lambda:  self.updateGaugeColorInnerRadius())

        self.ui.OuterRadiusSlider.valueChanged.connect( lambda:  self.updateGaugeColorOuterRadius())

        self.ui.offsetSlider.valueChanged.connect( lambda:  self.updateAngleOffset())

        self.ui.MinValueSlider.valueChanged.connect( lambda:  self.updateMinVal())

        self.ui.MaxValueSlider.valueChanged.connect( lambda:  self.updateMaxVal())

        self.ui.MainGridSlider.valueChanged.connect( lambda:  self.updateScalaCount())

        

        

        ################################################################################################
        # Update RGBA LCD value text color indicators
        ################################################################################################
        self.ui.lcdNumber_Red_Display.display(self.ui.RedSlider_Display.value())
        self.ui.lcdNumber_Green_Display.display(self.ui.GreenSlider_Display.value())
        self.ui.lcdNumber_Blue_Display.display(self.ui.BlueSlider_Display.value())
        self.ui.lcdNumber_Trancparency_Display.display(self.ui.TrancSlider_Display.value())



        ################################################################################################
        # Show hide bar graph marker
        ################################################################################################
        self.ui.CB_barGraph.stateChanged.connect(self.en_disable_barGraph)

        ################################################################################################
        # Show hide scale value
        ################################################################################################
        self.ui.CB_ValueText.stateChanged.connect(self.en_disable_ValueText)

        ################################################################################################
        # Show hide center pointer
        ################################################################################################
        self.ui.CB_CenterPoint.stateChanged.connect(self.en_disable_CB_CenterPoint)

        ################################################################################################
        # Show hide gauge scale text
        ################################################################################################
        self.ui.CB_ScaleText.stateChanged.connect(self.en_disable_ScaleText)

        ################################################################################################
        # Show hide bar graph
        ################################################################################################
        self.ui.CB_ShowBarGraph.stateChanged.connect(self.setEnableScalePolygon)

        ################################################################################################
        # Show hide long grid scale divisions
        ################################################################################################
        self.ui.CB_Grid.stateChanged.connect(self.set_enable_Scale_Grid)

        ################################################################################################
        # Show hide fine scale divisions
        ################################################################################################
        self.ui.CB_fineGrid.stateChanged.connect(self.set_enable_fine_Scale_Grid)

        ################################################################################################
        # Show hide needle/scale pointer
        ################################################################################################
        self.ui.CB_Needle.stateChanged.connect(self.en_disable_Needle)


        ################################################################################################
        # Select gauge theme
        ################################################################################################
        # self.ui.widget.setGaugeTheme(0)

        # self.ui.widget.setCustomGaugeTheme(
        #     color1 = "#FF2B00",
        #     color2= "#821600",
        #     color3 = "#260600"
        # )

        self.ui.widget.setCustomGaugeTheme(
            color1 = "#002523",
            color2= "#990008",
            color3 = "#00F6E9"
        )

        # self.ui.widget.setCustomGaugeTheme(
        #     color1 = "#fff",
        #     color2= "#555",
        #     color3 = "#000"
        # )

        # self.ui.widget.setScalePolygonColor(
        #     color1 = "red"
        # )

        # self.ui.widget.setNeedleCenterColor(
        #     color1 = "red"
        # )

        # self.ui.widget.setOuterCircleColor(
        #     color1 = "red"
        # )

        self.ui.widget.setBigScaleColor("#005275")
        self.ui.widget.setFineScaleColor("#005275")

        for x in range(1, 25):
            self.ui.theme_comboBox.addItem(str(x))


        ################################################################################################
        # Set custom font
        ################################################################################################
        QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), 'fonts/ds_digital/DS-DIGIB.TTF') )

        # self.ui.widget.setValueFontFamily("DS-Digital")
        # self.ui.widget.setScaleFontFamily("Verdana")

        ################################################################################################
        # Change gauge theme
        ################################################################################################
        self.ui.theme_comboBox.currentTextChanged.connect(lambda: self.changeGaugeTheme())

        self.updateGaugeValue()       

        ################################################################################################
        # END
        ################################################################################################

    def changeGaugeTheme(self):
        print(self.ui.theme_comboBox.currentText())
        self.ui.widget.setGaugeTheme(int(self.ui.theme_comboBox.currentText()))

    def updateScalaCount(self):
        self.ui.widget.setScalaCount(self.ui.MainGridSlider.value())
        self.ui.lcdScalaCount.display(int(self.ui.MainGridSlider.value()))    

    def updateMaxVal(self):
        self.ui.widget.setMaxValue(self.ui.MaxValueSlider.value())
        self.ui.lcdMaxVal.display(int(self.ui.MaxValueSlider.value()))    

        self.ui.ActualValueSlider.setMaximum(self.ui.MaxValueSlider.value())
        

    def updateMinVal(self):
        self.ui.widget.setMinValue(self.ui.MinValueSlider.value())
        self.ui.lcdMinVal.display(int(self.ui.MinValueSlider.value()))  

        self.ui.ActualValueSlider.setMinimum(self.ui.MinValueSlider.value())  

    def updateAngleOffset(self):
        self.ui.widget.updateAngleOffset(self.ui.offsetSlider.value())
        self.ui.lcdGaugeOffset.display(int(self.ui.offsetSlider.value()))    

    def updateGaugeColorOuterRadius(self):
        self.ui.widget.setGaugeColorOuterRadiusFactor(self.ui.OuterRadiusSlider.value())
        self.ui.lcdOuterRadius.display(int(self.ui.OuterRadiusSlider.value()))        

    def updateGaugeColorInnerRadius(self):
        self.ui.widget.setGaugeColorInnerRadiusFactor(self.ui.InnenRadiusSlider.value())
        self.ui.lcdInnerRadius.display(int(self.ui.InnenRadiusSlider.value()))        

    def updateStartScaleAngle(self):
        self.ui.widget.setScaleStartAngle(self.ui.GaugeStartSlider.value())
        self.ui.lcdGaugeStart.display(int(self.ui.GaugeStartSlider.value()))

    def updateScaleAngleSize(self):
        self.ui.widget.setTotalScaleAngleSize(self.ui.GaugeSizeSlider.value())
        self.ui.lcdGaugeSize.display(int(self.ui.GaugeSizeSlider.value()))

    def updateSliderValue(self):
        self.ui.ActualValueSlider.setValue(int(self.ui.widget.value))
        self.ui.lcdGaugeValue.display(int(self.ui.widget.value))
        self.ui.ActualValue.display(int(self.ui.widget.value))

    def updateGaugeValue(self):
        self.ui.widget.updateValue(self.ui.ActualValueSlider.value())
        self.ui.lcdGaugeValue.display(int(self.ui.widget.value))
        self.ui.ActualValue.display(int(self.ui.widget.value))

    ################################################################################################
    # SET NEEDLE COLOR
    ################################################################################################
    def setNeedleColor(self):
        # Get RGBA values from sliders
        R = self.ui.RedSlider_Needle.value()
        G = self.ui.GreenSlider_Needle.value()
        B = self.ui.BlueSlider_Needle.value()
        Transparency = self.ui.TrancSlider_Needle.value()
        # print(R, G, B, Transparency)
        self.ui.widget.setNeedleColor(R=R, G=G, B=B, Transparency=Transparency)

    ################################################################################################
    # SET NEEDLE COLOR ON DRAG
    ################################################################################################
    def setNeedleColorOnDrag(self):
        # Get RGBA values from sliders
        R = self.ui.RedSlider_NeedleDrag.value()
        G = self.ui.GreenSlider_NeedleDrag.value()
        B = self.ui.BlueSlider_NeedleDrag.value()
        Transparency = self.ui.TrancSlider_NeedleDrag.value()
        # print(R, G, B, Transparency)
        self.ui.widget.setNeedleColorOnDrag(R=R, G=G, B=B, Transparency=Transparency)


    ################################################################################################
    # SET SCALE TEXT COLOR
    ################################################################################################
    def setScaleValueColor(self):
        # Get RGBA values from sliders
        R = self.ui.RedSlider_Scale.value()
        G = self.ui.GreenSlider_Scale.value()
        B = self.ui.BlueSlider_Scale.value()
        Transparency = self.ui.TrancSlider_Scale.value()
        # print(R, G, B, Transparency)
        self.ui.widget.setScaleValueColor(R=R, G=G, B=B, Transparency=Transparency)


    ################################################################################################
    # SET VALUE DISPLAY COLOR
    ################################################################################################
    def setDisplayValueColor(self):
        # GET RGBA VALUE
        R = self.ui.RedSlider_Display.value()
        G = self.ui.GreenSlider_Display.value()
        B = self.ui.BlueSlider_Display.value()
        Transparency = self.ui.TrancSlider_Display.value()
        # print(R, G, B, Transparency)
        self.ui.widget.setDisplayValueColor(R=R, G=G, B=B, Transparency=Transparency)

    ################################################################################################
    # SHOW HIDE BAR GRAPH
    ################################################################################################
    def en_disable_barGraph(self):
        self.ui.widget.setEnableBarGraph(self.ui.CB_barGraph.isChecked())

    ################################################################################################
    # SHOW HIDE VALUE TEXT
    ################################################################################################
    def en_disable_ValueText(self):
        self.ui.widget.setEnableValueText(self.ui.CB_ValueText.isChecked())

    ################################################################################################
    # SHOW HIDE CENTER POINTER
    ################################################################################################
    def en_disable_CB_CenterPoint(self):
        self.ui.widget.setEnableCenterPoint(self.ui.CB_CenterPoint.isChecked())

    ################################################################################################
    # SHOW HIDE NEEDLE
    ################################################################################################
    def en_disable_Needle(self):
        self.ui.widget.setEnableNeedlePolygon(self.ui.CB_Needle.isChecked())

    ################################################################################################
    # SHOW HIDE SCALE TEXT
    ################################################################################################
    def en_disable_ScaleText(self):
        self.ui.widget.setEnableScaleText(self.ui.CB_ScaleText.isChecked())

    ################################################################################################
    # ENABLE DISABLE FILL COLOR
    ################################################################################################
    def setEnableScalePolygon(self):
        self.ui.widget.setEnableScalePolygon(self.ui.CB_ShowBarGraph.isChecked())

    ################################################################################################
    # ENABLE DISABLE BIG SCALE
    ################################################################################################
    def set_enable_Scale_Grid(self):
        self.ui.widget.setEnableBigScaleGrid(self.ui.CB_Grid.isChecked())

    ################################################################################################
    # ENABLE DISABLE FINE SCALE MARKERS
    ################################################################################################
    def set_enable_fine_Scale_Grid(self):
        self.ui.widget.setEnableFineScaleGrid(self.ui.CB_fineGrid.isChecked())


########################################################################
## EXECUTE APP
########################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

########################################################################
## END===>
########################################################################  