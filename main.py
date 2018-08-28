from PyQt5 import QtQml, QtWidgets, QtGui, QtCore
from weather import Weather, Unit
import sys

#---------------------------------------------#
# weather setup + variables to use in classes #
#---------------------------------------------#

mainLocation = "warsaw"

#weather setup, units, location and the conditions
weather = Weather(unit = Unit.CELSIUS)
weatherLocation = weather.lookup_by_location(mainLocation)
weatherCondition = weatherLocation.condition
weatherForecast = weatherLocation.forecast

#----------------------------#
# main window class with QML #
#----------------------------#
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    #---------------------------------------------#
    # main function that can be output trough QML #
    #---------------------------------------------#
    @QtCore.pyqtSlot(result = str)
    def mainWeather(self):
        #final output
        weatherFullString = "Today it's " + self.mainWeatherDate() + ", we have " + self.mainWeatherTemp() + " and a " + self.mainWeatherStatus() + " day."
        return weatherFullString
    
    #-----------------------------------------#
    # main date that can be output trough QML #
    #-----------------------------------------#
    @QtCore.pyqtSlot(result = str)
    def mainWeatherDate(self):
        weatherDate = weatherCondition.date
        return weatherDate
    
    #-----------------------------------------#
    # main temp that can be output trough QML #
    #-----------------------------------------#
    @QtCore.pyqtSlot(result = str)
    def mainWeatherTemp(self):
        weatherTemp = weatherCondition.temp + "°"
        return weatherTemp
    
    #----------------------------------------------#
    # main condition that can be output trough QML #
    #----------------------------------------------#
    @QtCore.pyqtSlot(result = str)
    def mainWeatherStatus(self):
        weatherStatus = weatherCondition.text
        return weatherStatus

#-------------------#
# app setup for QML #
#-------------------#
app = QtWidgets.QApplication(sys.argv)
window = Window()
engine = QtQml.QQmlApplicationEngine()
engine.rootContext().setContextProperty("window", window)
engine.load("main.qml")

engine.quit.connect(app.quit)

sys.exit(app.exec_())
