GLOBAL TIME IN CITIES:
Code:

import pytz
from datetime import datetime

def get_city_time(city, timezone):
    city_time = datetime.now(pytz.timezone(timezone))
    return city_time.strftime(f"%Y-%m-%d %H:%M:%S {city}")

cities = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
    "Mumbai": "Asia/Kolkata"
}

for city, timezone in cities.items():
    print(get_city_time(city, timezone))


 Expected Output:

2025-07-17 07:28:00 New York
2025-07-17 12:28:00 London
2025-07-18 00:28:00 Tokyo
2025-07-18 02:28:00 Sydney
2025-07-17 17:58:00 Mumbai