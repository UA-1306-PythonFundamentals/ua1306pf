from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

def weather (API_KEY, City):
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()


    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(City)
    w = observation.weather
    return f"""detailed_status: {w.detailed_status}

humidity: {w.humidity}

wind: {w.wind()}

temperature in celsius: {w.temperature('celsius')}

rain: {w.rain}

heat_index: {w.heat_index}

clouds: {w.clouds}"""



