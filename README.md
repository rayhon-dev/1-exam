Weather API

This API provides weather data management and analytics functionalities.

Installation

Clone the repository:

git clone <repository_url>
cd <project_directory>

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Apply database migrations:

python manage.py migrate

Start the development server:

python manage.py runserver

API Endpoints

Locations

GET /api/locations/ - Retrieve all locations

POST /api/locations/ - Create a new location

GET /api/locations/{id}/ - Retrieve a specific location

PUT /api/locations/{id}/ - Update a location

DELETE /api/locations/{id}/ - Delete a location

Weather Data

GET /api/weather-data/ - Retrieve all weather data

POST /api/weather-data/ - Add new weather data

GET /api/weather-data/{id}/ - Retrieve a specific weather data entry

PUT /api/weather-data/{id}/ - Update weather data

DELETE /api/weather-data/{id}/ - Delete weather data

GET /api/weather-data/location/{location_id}/ - Retrieve weather data for a specific location

Weather Analytics

GET /api/weather-data/analytics/temperature-avg/ - Get average temperature across all locations

GET /api/weather-data/analytics/precipitation-sum/ - Get total precipitation

GET /api/weather-data/analytics/wind-speed-max/ - Get maximum wind speed recorded

Forecasts

GET /api/forecasts/ - Retrieve all forecasts

POST /api/forecasts/ - Create a new forecast

GET /api/forecasts/{id}/ - Retrieve a specific forecast

PUT /api/forecasts/{id}/ - Update a forecast

DELETE /api/forecasts/{id}/ - Delete a forecast

GET /api/forecasts/location/{location_id}/ - Retrieve forecasts for a specific location