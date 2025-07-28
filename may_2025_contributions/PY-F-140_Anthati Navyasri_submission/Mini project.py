GLOBAL TIME IN CITIES PROJECT:

from datetime import datetime
import pytz
def get_time_in_timezone(timezone):
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    return current_time
# Example usage
print(get_time_in_timezone('US/Pacific'))
print(get_time_in_timezone('Asia/Kolkata'))

expected output:
2025-07-17 01:58:12.079049-07:00
2025-07-17 14:28:12.080409+05:30