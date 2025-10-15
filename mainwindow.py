from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
import requests


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")

        self.central_widget = MainWidget()
        self.setCentralWidget(self.central_widget)

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
