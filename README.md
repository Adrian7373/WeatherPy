# 🌦️ WeatherPy

A simple and elegant **Python Weather Application** built using **PySide6 (Qt for Python)** and the **WeatherAPI**.
This program allows users to enter any city or location name, fetches real-time weather data via an API request, and displays the information inside a modern GUI window.

---

## 🧠 Overview

WeatherPy demonstrates how to integrate **APIs** with a **graphical user interface (GUI)** in Python.
It retrieves live weather data such as temperature, humidity, condition, and wind speed using **WeatherAPI**, and displays the results dynamically in the window.

---

## 🖥️ Features

✅ User-friendly GUI made with **PySide6**
✅ Real-time weather data fetching via **requests**
✅ Displays detailed weather information:

* Location name (city, region, country)
* Local time
* Temperature (with "feels like" temperature)
* Weather condition
* Wind speed
* Humidity
* Heat index

✅ Error handling for:

* Missing input (no place entered)
* Network or API errors

✅ Centered main window on screen

---

## 🧩 Technologies Used

* **Python 3**
* **PySide6** — for GUI
* **Requests** — for making API calls
* **WeatherAPI** — for weather data

---

## 📂 File Structure

```
WeatherPy/
│
├── main.py             # Entry point of the application
├── mainwindow.py       # Contains MainWindow, MainWidget, and Weather classes
└── README.md           # Project documentation
```

---

## ⚙️ How It Works

1. The user enters a **place name** (e.g., “Tokyo”, “London”, “Manila”).
2. The app sends a **GET** request to the WeatherAPI endpoint:

   ```
   https://api.weatherapi.com/v1/current.json?q=<place>&key=<your_api_key>
   ```
3. The program parses the JSON response using `requests`.
4. Weather information is displayed in neatly arranged **QLabels** within the main window.

---

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/Adrian7373/WeatherPy.git
   ```
2. Navigate into the project folder:

   ```bash
   cd WeatherPy
   ```
3. Install dependencies:

   ```bash
   pip install PySide6 requests
   ```
4. Run the app:

   ```bash
   python main.py
   ```

---

## 🧱 Class Overview

### `MainWindow(QMainWindow)`

* The main GUI window.
* Contains input field (`QLineEdit`), buttons, and display labels.
* Handles user input and calls the `Weather` class to retrieve data.

### `MainWidget(QWidget)`

* Provides a vertical layout (`QVBoxLayout`) for organizing widgets in the main window.

### `Weather`

* Handles API communication using `requests`.
* Parses JSON responses and stores the weather information for easy access.

---

## ⚠️ Error Handling

* If the user leaves the input blank → shows a `QMessageBox.information()` popup asking for a place name.
* If there’s a network issue or API request failure → shows a `QMessageBox.information()` alert with a “Network Error” message.

---

## 📸 Future Improvements

* Add weather icons (sunny, cloudy, rainy, etc.)
* Display forecast (3-day or 7-day)
* Improve layout with CSS-style Qt stylesheets
* Add light/dark mode toggle

---

## 👨‍💻 Author

**Adrian Ablaza**
📚 IT Student | 🧠 Aspiring Full-Stack Developer
💻 Passionate about Python, APIs, and modern UI design
