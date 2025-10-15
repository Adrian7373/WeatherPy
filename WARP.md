# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Commands

- Install dependencies
  ```bash path=null start=null
  pip install PySide6 requests
  ```
- Run the app
  ```bash path=null start=null
  python main.py
  ```
- Linting
  - No linter is configured in this repo.
- Tests
  - No tests are present in this repo.
  - If/when pytest is added, run the suite or a single test like:
    ```bash path=null start=null
    pytest -q
    pytest -q -k "pattern"           # subset by name
    pytest -q tests/test_file.py::TestClass::test_case
    ```

## Architecture overview

- Entry point: `main.py`
  - Creates the Qt application and launches the main window.
- UI layer: `ui_main.py`
  - PySide6 widgets built around `QMainWindow` with a central `QWidget`, menu bar, and toolbar.
- Weather/API layer: `weather.py`
  - Encapsulates WeatherAPI access using `requests`.
  - Provides methods to fetch current weather by city/location and returns parsed data to the UI.
  - Handles request/response errors; the UI surfaces failures via `QMessageBox`.
- Data flow
  - User action in the UI → call into `weather.py` → HTTP GET to WeatherAPI → parse JSON → update UI labels/fields.
- API key
  - The README indicates an API key is referenced in `weather.py` (e.g., `self.api_key = "..."`).

## Repo notes

- Important docs: see `README.md` (features, setup, how it works) and `LICENSE` (MIT).
- No CLAUDE, Cursor, or Copilot rule files detected.
