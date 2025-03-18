# Weather API

This API provides weather data management and analytics functionalities.

---

## 📌 Installation

### 1️⃣ Clone the repository:
```sh
git clone <repository_url>
cd <project_directory>

2️⃣ Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3️⃣ Install dependencies:

pip install -r requirements.txt
4️⃣ Apply database migrations:

python manage.py migrate
5️⃣ Start the development server:

python manage.py runserver
📡 API Endpoints

🌍 Locations

Method	Endpoint	Description

GET	/api/locations/	Retrieve all locations
POST	/api/locations/	Create a new location
GET	/api/locations/{id}/	Retrieve a specific location
PUT	/api/locations/{id}/	Update a location
DELETE	/api/locations/{id}/	Delete a location

🌦️ Weather Data

Method	Endpoint	Description

GET	/api/weather-data/	Retrieve all weather data
POST	/api/weather-data/	Add new weather data
GET	/api/weather-data/{id}/	Retrieve a specific weather data entry
PUT	/api/weather-data/{id}/	Update weather data
DELETE	/api/weather-data/{id}/	Delete weather data
GET	/api/weather-data/location/{id}/	Retrieve weather data for a specific location

📊 Weather Analytics

Method	Endpoint	Description
GET	/api/weather-data/analytics/temperature-avg/	Get average temperature across all locations
GET	/api/weather-data/analytics/precipitation-sum/	Get total precipitation
GET	/api/weather-data/analytics/wind-speed-max/	Get maximum wind speed recorded

⛅ Forecasts

Method	Endpoint	Description

GET	/api/forecasts/	Retrieve all forecasts
POST	/api/forecasts/	Create a new forecast
GET	/api/forecasts/{id}/	Retrieve a specific forecast
PUT	/api/forecasts/{id}/	Update a forecast
DELETE	/api/forecasts/{id}/	Delete a forecast
GET	/api/forecasts/location/{id}/	Retrieve forecasts for a specific location

⚙️ Technologies Used

Django REST Framework (DRF) - API development
Python - Core programming language
SQLite / PostgreSQL - Database management
Git & GitHub - Version control
Docker (optional) - Containerization

🚀 How to Contribute
Fork this repository.

Create a new branch (feature-branch).
Commit your changes.
Push to your fork and submit a Pull Request.
