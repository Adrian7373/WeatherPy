from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import requests


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
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

    def retrieveData(self):
        place = self.placeName.text().strip()
        if not place:
            self.central_widget.layout.addWidget(QMessageBox.information(self,
                                                                         "Error", "Please enter a place name!", QMessageBox.Ok))

        try:
            weather = Weather(place)
        except SystemExit as e:
            self.central_widget.layout.addWidget(
                QMessageBox.information(self, "Error", "Network Error", QMessageBox.Ok))

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

    def centerOnScreen(self):
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
    def __init__(self, placeName):
        self.placeName = placeName
        self.api_key = 'your_api_key'

        try:
            response = requests.get(
                f"https://api.weatherapi.com/v1/current.json?q={placeName}&key={self.api_key}")
            response.raise_for_status()
            weather_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            raise SystemExit(f"Network Error: could not fetch weather data")

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
