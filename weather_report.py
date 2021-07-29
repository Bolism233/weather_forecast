import pyowm
from pyowm.utils import timestamps
from pyzipcode import ZipCodeDatabase
from Api_key import api_key

# todo
# Next steps: Make it so the program can take in user inputs, for example, enter in a zip code, and if they want today or tomorrow's weather
# After that, if the user chooses today's weather, tell them if they need to bring an umbrella or not. If you can't currently find out if it will rain today, make it so you can. There probably won't be data say says "it will rain" or "it will not rain", it will probably be chance of precipitation. So you will have to take that text and figure out if above 30% chance you should just tell the user to bring an umbrella anyways

zipcode = '11355'
# zipcode = input("What is your zipcode?\n") # commented out since annoying to type every time
date = input("Do you want the weather for today or tomorrow?\n")

zcdb = ZipCodeDatabase()
zipcode = zcdb[zipcode].city #find out the city name based on zipcode

owm = pyowm.OWM(api_key)
mgr = owm.weather_manager()

def temperature_and_humidity():
    temp = weather.temperature('celsius')
    for key, value in temp.items():
        print(key, value)
    humid = weather.humidity
    print("Humidity: " + str(humid))


def is_rainy():
   if weather.status.lower() == 'rain':
       print("Be sure to bring an umbrella, it is going to rain.")

if date.lower() == 'today':
    zipcode = mgr.weather_at_place(zipcode)
    weather = zipcode.weather
    print("The weather status: " + weather.status.lower() + ".")
    is_rainy()
    temperature_and_humidity()

elif date.lower() == 'tomorrow':
    three_h_forecast = mgr.forecast_at_place(zipcode, '3h')
    tomorrow = timestamps.tomorrow()  # datetime object for tomorrow
    weather = three_h_forecast.get_weather_at(tomorrow)
    print("The weather status for tomorrow is " + weather.status.lower() + ".")
    is_rainy()
    temperature_and_humidity()

