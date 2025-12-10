#!usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter
import ttkbootstrap as ttk
import openmeteo_requests
import os

# $filepath
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)

# $dictdef
code_int_to_png = {
    0: "sunny",
    1: "mostly_sunny",
    2: "partly_cloudy",
    3: "cloudy",
    45: "haze_fog_dust_smoke",
    48: "haze_fog_dust_smoke",
    51: "drizzle",
    53: "showers_rain",
    55: "heavy_rain",
    56: "wintry_mix_rain_snow",
    57: "wintry_mix_rain_snow",
    61: "drizzle",
    63: "showers_rain",
    65: "heavy_rain",
    66: "wintry_mix_rain_snow",
    67: "wintry_mix_rain_snow",
    71: "flurries",
    73: "snow_showers_snow",
    75: "heavy_snow",
    77: "sleet_hail",
    80: "drizzle",
    81: "showers_rain",
    82: "heavy_rain",
    85: "snow_showers_snow",
    86: "heavy_snow",
    95: "isolated_scattered_tstorms_day",
    96: "strong_tstorms",
    97: "strong_tstorms",
    100: "clear_night",
    101: "mostly_clear_night",
    102: "partly_cloudy_night",
    103: "cloudy",
    145: "haze_fog_dust_smoke",
    148: "haze_fog_dust_smoke",
    151: "drizzle",
    153: "showers_rain",
    155: "heavy_rain",
    156: "wintry_mix_rain_snow",
    157: "wintry_mix_rain_snow",
    161: "drizzle",
    163: "showers_rain",
    165: "heavy_rain",
    166: "wintry_mix_rain_snow",
    167: "wintry_mix_rain_snow",
    171: "flurries",
    173: "snow_showers_snow",
    175: "heavy_snow",
    177: "sleet_hail",
    180: "drizzle",
    181: "showers_rain",
    182: "heavy_rain",
    185: "snow_showers_snow",
    186: "heavy_snow",
    195: "isolated_scattered_tstorms_night",
    196: "strong_tstorms",
    197: "strong_tstorms"
}

# $openmeteoreq
openmeteo = openmeteo_requests.Client()
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 7.0903,
	"longitude": -70.7617,
	"current": ["is_day", "temperature_2m", "weather_code"],
	"timezone": "America/New_York",
}

# $reqparse
responses = openmeteo.weather_api(url, params=params)
response = responses[0]
curr = response.Current()
currisdayfloat = curr.Variables(0).Value()
currisday = "day" if currisdayfloat == 1.0 else "night"
currtempfloat = curr.Variables(1).Value()
currtemp = "{:.2f}".format(currtempfloat)
currcodefloat = curr.Variables(2).Value()
currcode = int(currcodefloat)

# $createwin
try:
    weather_root = ttk.Window(themename = "lightmaterial2" if currisday == "day" else "darkmaterial2")
except tkinter.TclError:
    weather_root = ttk.Window(themename = "litera" if currisday == "day" else "darkly")
weather_root.overrideredirect(1)
weather_root.geometry("200x250+400+0")

# $refresh
def refresh():
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    curr = response.Current()
    currisdayfloat = curr.Variables(0).Value()
    currisday = "day" if currisdayfloat == 1.0 else "night"
    currtempfloat = curr.Variables(1).Value()
    currtemp = int(currtempfloat)
    currcodefloat = curr.Variables(2).Value()
    currcode = int(currcodefloat)
    style = ttk.Style()
    try:
        style.theme_use("lightmaterial2" if currisday == "day" else "darkmaterial2")
    except tkinter.TclError:
        style.theme_use("litera" if currisday == "day" else "darkly")
    temperature_l.config(text = f"{currtemp} °C")
    temperature_l.after(900000, refresh)
    weathericon_ph.config(file = f"{script_directory}\\data\\{code_int_to_png[currcode + (1 - int(currisdayfloat)) * 100]}.png")


# $temperature
temperature_l = ttk.Label(master = weather_root, font = "Ubuntu 24")
temperature_l.pack()

# $weathericon
weathericon_ph = ttk.PhotoImage()
weathericon_l = ttk.Label(master = weather_root, image = weathericon_ph)
weathericon_l.pack()

# $runfunc
refresh()

# $mainloop
weather_root.mainloop()
