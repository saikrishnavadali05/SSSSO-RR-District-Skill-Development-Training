#Mini Project : Global Time in Cities (API)
#Date : 13 July 2025
#Author : Praveena Kumbum
#Description : Shows the current time in different time zones or cities. 
#The program fetches time data (e.g. from the World Time API) for a list of cities and displays it.
#Uses time API (e.g. http://worldtimeapi.org/api/timezone/America/New_York) 

import requests
import tkinter
from tkinter import ttk, messagebox

# Main Window
root = tkinter.Tk()
root.title("Global Time in Cities")
root.geometry("350x200")

#Function for capturing the details submitted in field city
#Sending a GET request to API and receving the response JSON or error code.
def OnClick():
    city = City_Dropdown.get().strip()
    timezone = city.split(':')[0].strip()
    
    try:
        response = requests.get(f"https://timeapi.io/api/Time/current/zone?timeZone={timezone}", timeout=5)
        
        if response.status_code == 200:
            data = response.json() #Data Parsing
            date = data.get('date','Not found')
            time = data.get('time', 'Not found')
            day = data.get('dayOfWeek', 'Not found')
            
            #Displaying the current date time details in message box
            messagebox.showinfo("Current Time", 
                                 f"Current date and Time details of {city} are as below: \n"
                                 f"Date       : {date}\n"
                                 f"Time       : {time}\n"
                                 f"Day        : {day}")
        else:
            messagebox.showerror("API Error", f"Failed to fetch time.\nStatus code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Connection Error", f"Unable to connect:\n{e}")

#City/Timezone dropdown
City_Label = tkinter.Label(root, text="Select City / Time Zone")
City_Label.pack(pady=20)

TimeZones = ['Asia/Kolkata : India',
            'Asia/Dubai : UAE',
            'Asia/Tokyo : Japan',
            'Asia/Shanghai : China',
            'Asia/Singapore : Singapore',
            'Asia/Seoul : South Korea',
            'Asia/Bangkok : Thailand',
            'Asia/Kathmandu : Nepal',
            'Asia/Tehran : Iran',
            'Asia/Jakarta : Indonesia (Java/Bali)',
            'Asia/Baghdad : Iraq',
            'Asia/Karachi : Pakistan',
            'Europe/London : United Kingdom',
            'Europe/Berlin : Germany',
            'Europe/Paris : France',
            'Europe/Moscow : Russia',
            'Europe/Madrid : Spain',
            'Europe/Rome : Italy',
            'Europe/Istanbul : Turkey',
            'Europe/Amsterdam : Netherlands',
            'Europe/Zurich : Switzerland',
            'Europe/Warsaw : Poland',
            'America/New_York : Eastern Time (US)',
            'America/Chicago : Central Time (US)',
            'America/Denver : Mountain Time (US)',
            'America/Los_Angeles : Pacific Time (US)',
            'America/Phoenix : Arizona (no DST)',
            'America/Toronto : Canada',
            'America/Sao_Paulo : Brazil',
            'America/Mexico_City : Mexico',
            'America/Bogota : Colombia',
            'America/Argentina/Buenos_Aires : Argentina',
            'Africa/Cairo : Egypt',
            'Africa/Nairobi : Kenya',
            'Africa/Lagos : Nigeria',
            'Africa/Johannesburg : South Africa',
            'Africa/Casablanca : Morocco',
            'Australia/Sydney : Australia (East)',
            'Australia/Perth : Australia (West)',
            'Australia/Adelaide : Australia (Central)',
            'Pacific/Auckland : New Zealand',
            'Pacific/Fiji : Fiji',
            'Pacific/Honolulu : Hawaii (US)']

City_Dropdown = ttk.Combobox(root, values=TimeZones)
City_Dropdown.pack()
City_Dropdown.current(0)  # Default selection

#CurrentTime BUtton
CurrentTime_Button = tkinter.Button(root, text="Current Time", command=OnClick,font=("Arial", 12), bg="#4CAF50", fg="white" )
CurrentTime_Button.pack(pady=20)

root.mainloop()