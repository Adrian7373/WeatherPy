from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMenuBar, QMessageBox
import requests


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Weather App")

        self.central_widget = MainWidget()
        self.setCentralWidget(self.central_widget)

        menu_bar = QMenuBar()
        app_menu = menu_bar.addMenu("Menu")
        quit_action = app_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_clicked)
        self.central_widget.layout.addWidget(menu_bar)

    def quit_clicked(self):
        message = QMessageBox()
        message.setWindowTitle("Quit App")
        message.setMinimumSize(700, 200)
        message.setInformativeText("Do you want to quit the app?")
        message.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Yes)
        ret = message.exec()
        if ret == QMessageBox.Yes:
            self.quitApp()
        else:
            print("user chose cancel")

    def quitApp(self):
        self.app.quit()

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
