from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel,
                               QLineEdit, QPushButton, QMessageBox, QApplication)
from PySide6.QtCore import QRect, QPoint
import requests
from typing import Dict, Any, Optional
from config import WEATHER_API_KEY


class MainWindow(QMainWindow):
    def __init__(self, app: QApplication) -> None:
        super().__init__()
        self.app: QApplication = app
        self.setWindowTitle("Weather App")

        self.placeLabel = QLabel()
        self.localtime = QLabel()
        self.temparature = QLabel()
        self.condition = QLabel()
        self.windspeed = QLabel()
        self.humidity = QLabel()
        self.heat_index = QLabel()
        self.central_widget = MainWidget()

        self.setCentralWidget(self.central_widget)
        self.label = QLabel("Enter place name: ")
        self.placeName = QLineEdit()
        self.submitButton = QPushButton("Start")
        self.submitButton.clicked.connect(self.retrieveData
                                          )

        self.central_widget.layout.addWidget(self.label)
        self.central_widget.layout.addWidget(self.placeName)
        self.central_widget.layout.addWidget(self.submitButton)

        self.central_widget.layout.addWidget(self.placeLabel)
        self.central_widget.layout.addWidget(self.localtime)
        self.central_widget.layout.addWidget(self.temparature)
        self.central_widget.layout.addWidget(self.condition)
        self.central_widget.layout.addWidget(self.windspeed)
        self.central_widget.layout.addWidget(self.humidity)
        self.central_widget.layout.addWidget(self.heat_index)

    def retrieveData(self) -> None:
        place: str = self.placeName.text().strip()
        if not place:
            QMessageBox.information(
                self, "Error", "Please enter a place name!", QMessageBox.Ok)
            return

        try:
            weather = Weather(place)
        except SystemExit:
            QMessageBox.information(
                self, "Error", "Network Error", QMessageBox.Ok)
            return

        self.placeLabel.setText(f"<b>Place:</b> {weather.locationName}, {weather.regionName}, {weather.countryName}"
                                )
        self.localtime.setText(f"<b>LocalTime:</b> {weather.localTime}")
        self.temparature.setText(
            f"<b>Temperature:</b> {weather.tempC}°C (Feels like: {weather.feelslikeC}°C)"
        )
        self.condition.setText(f"<b>Condition:</b> {weather.condition}")
        self.windspeed.setText(f"<b>Wind Speed:</b> {weather.windSpeed} kph")
        self.humidity.setText(f"<b>Humidity:</b> {weather.humidity}%")
        self.heat_index.setText(f"<b>Heat Index:</b> {weather.heatindexC}°C")

    def centerOnScreen(self) -> None:
        frame_geom = self.frameGeometry()
        screen_center = self.screen().availableGeometry().center()
        frame_geom.moveCenter(screen_center)
        self.move(frame_geom.topLeft())


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)


class Weather:
    def __init__(self, placeName: str) -> None:
        self.placeName: str = placeName
        self.locationName: str = ""
        self.regionName: str = ""
        self.countryName: str = ""
        self.tempC: float = 0.0
        self.condition: str = ""
        self.windSpeed: float = 0.0
        self.humidity: int = 0
        self.feelslikeC: float = 0.0
        self.heatindexC: float = 0.0
        self.localTime: str = ""

        try:
            response = requests.get(
                f"https://api.weatherapi.com/v1/current.json?q={placeName}&key={WEATHER_API_KEY}",
                timeout=10)  # Add 10 second timeout
            response.raise_for_status()
            weather_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            raise SystemExit(
                "Network Error: could not fetch weather data") from e

        # Store weather data
        self.locationName = weather_data['location']['name']
        self.regionName = weather_data['location']['region']
        self.countryName = weather_data['location']['country']
        self.tempC = weather_data['current']['temp_c']
        self.condition = weather_data['current']['condition']['text']
        self.windSpeed = weather_data['current']['wind_kph']
        self.humidity = weather_data['current']['humidity']
        self.feelslikeC = weather_data['current']['feelslike_c']
        self.heatindexC = weather_data['current']['heatindex_c']
        self.localTime = weather_data['location']['localtime']
