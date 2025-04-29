# Weather Forecasting Web Application

A simple weather forecasting web application built with Django. This app allows users to search for weather information for any city and view real-time weather data including temperature, humidity, and weather conditions.

## Features

- Search for weather data by city name.
- Displays current weather conditions: temperature, humidity, and weather description.
- Built with Django and the OpenWeatherMap API.

## Tech Stack

- **Backend:** Django 5.2
- **Frontend:** HTML, CSS
- **API:** OpenWeatherMap API for fetching weather data
- **Database:** SQLite (or any other preferred database)

## Installation

### Prerequisites

- Python 3.x
- Django 5.2
- Requests library for API calls

### Steps to Install Locally

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/weatherapp.git
    cd weatherapp
    ```

2. Create a virtual environment:

    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure the OpenWeatherMap API key:
    - Sign up at [OpenWeatherMap](https://openweathermap.org/) and get an API key.
    - Add your API key to `settings.py` or use environment variables.

5. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Visit the app at `http://127.0.0.1:8000` in your browser.

## Usage

1. On the homepage, enter the name of a city in the search bar.
2. The weather data for that city will be displayed, including the temperature, humidity, and weather conditions.

## Deployment

For deployment instructions, you can follow these steps:
- **For PythonAnywhere:** 
    - Follow the deployment guide specific to PythonAnywhere.
- **For other platforms like Heroku or Railway:**
    - Follow the respective platform's Django deployment guide.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
