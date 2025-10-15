# 🌤️ WeatherPy — A Simple Weather Application Built with PySide6

WeatherPy is a clean and responsive **desktop weather application** built with **Python (PySide6)**.
It fetches real-time weather data using the [WeatherAPI](https://www.weatherapi.com/) and displays it in a user-friendly interface.

---

## 🖥️ Features

* 🌍 Fetches live weather data by **city name or location**
* 🌡️ Displays **temperature, condition, humidity, and wind speed**
* 🪟 Built with **PySide6 (Qt for Python)** — smooth native desktop UI
* ⚙️ Includes **menu bar** and **toolbar** for better navigation
* 🧩 Modular design using **QMainWindow** and **QWidget**
* 💬 Graceful error handling for invalid requests or no internet connection

---

## 🧰 Tech Stack

| Category      | Technology                                                              |
| ------------- | ----------------------------------------------------------------------- |
| Language      | Python 3.x                                                              |
| GUI Framework | PySide6                                                                 |
| API           | WeatherAPI ([https://www.weatherapi.com/](https://www.weatherapi.com/)) |
| HTTP Library  | Requests                                                                |

---

## 🚀 Getting Started

### 1️⃣ Clone this repository

```bash
git clone https://github.com/Adrian7373/WeatherPy.git
cd WeatherPy
```

### 2️⃣ Install dependencies

```bash
pip install PySide6 requests
```

### 3️⃣ Get your API key

Sign up at [WeatherAPI.com](https://www.weatherapi.com/) and copy your **API key**.

Then open the file (for example `weather.py`) and paste your key:

```python
self.api_key = "your_api_key_here"
```

### 4️⃣ Run the app

```bash
python main.py
```

---

## 📸 Screenshot (optional)

*(Add a screenshot of your main window here)*

```markdown
![WeatherPy Screenshot](assets/screenshot.png)
```

---

## 🧩 Project Structure

```
WeatherPy/
│
├── main.py            # Entry point — launches the app window
├── weather.py         # Contains the Weather class and API logic
├── ui_main.py         # UI components (MainWindow, MainWidget)
├── assets/            # (Optional) images or icons
└── README.md
```

---

## 🧠 How It Works

1. User enters a **city name** or location.
2. App sends a `GET` request to WeatherAPI using `requests`.
3. JSON response is parsed and displayed on the GUI.
4. If the network or API fails, a **QMessageBox** shows an error message.

---

## 📦 Future Improvements

* Add a **5-day forecast** tab
* Display **weather icons** dynamically
* Save recent searches
* Switch between °C / °F

---

## 🧑‍💻 Author

**Adrian Ablaza**
2nd Year BSIT Student – Nueva Ecija University of Science and Technology
Passionate about programming, UI design, and building Python applications.

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use and modify it.
