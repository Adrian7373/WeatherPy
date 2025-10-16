from PySide6.QtWidgets import QLabel, QApplication
from mainwindow import MainWindow, Weather
import sys
app = QApplication(sys.argv)

window = MainWindow(app)
placeName = input("Enter place name: ")

weather = Weather(placeName)

window.central_widget.layout.addWidget(QLabel(
    f"<b>Place:</b> {weather.locationName}, {weather.regionName}, {weather.countryName}"
))
window.central_widget.layout.addWidget(
    QLabel(f"<b>LocalTime:</b> {weather.localTime}"))
window.central_widget.layout.addWidget(QLabel(
    f"<b>Temperature:</b> {weather.tempC}°C (Feels like: {weather.feelslikeC}°C)"
))
window.central_widget.layout.addWidget(
    QLabel(f"<b>Condition:</b> {weather.condition}"))
window.central_widget.layout.addWidget(
    QLabel(f"<b>Wind Speed:</b> {weather.windSpeed} kph"))
window.central_widget.layout.addWidget(
    QLabel(f"<b>Humidity:</b> {weather.humidity}%"))
window.central_widget.layout.addWidget(
    QLabel(f"<b>Heat Index:</b> {weather.heatindexC}°C"))


window.show()
window.centerOnScreen()
app.exec()
