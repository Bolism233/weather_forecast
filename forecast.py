import requests
import pyowm
from pyowm.utils import timestamps
from pyzipcode import ZipCodeDatabase
from Api_key import api_key

choice = input("Do you want to run pyowm or owm?\n").lower()

def p_y_owm():

    while True:
        try:
            zcdb = ZipCodeDatabase()
            zipcode = input("What is your zipcode?\n")
            city_name = zcdb[zipcode].city  # find out the city name based on zipcode
            break
        except KeyError:
            print("Oops, not a valid input, try again!")

    date = input("Do you want the weather for today or tomorrow?\n")
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

    while True:
        if date.lower() == 'today':
            zip = mgr.weather_at_place(city_name)
            weather = zip.weather
            print("Today's weather status for " + str(zipcode) + " is " + weather.status.lower() + ".")
            is_rainy()
            temperature_and_humidity()
            break

        elif date.lower() == 'tomorrow':
            three_h_forecast = mgr.forecast_at_place(city_name, '3h')
            tomorrow = timestamps.tomorrow()  # datetime object for tomorrow
            weather = three_h_forecast.get_weather_at(tomorrow)
            print("Tomorrow's weather status for " + str(zipcode) + " is " + weather.status.lower() + ".")
            is_rainy()
            temperature_and_humidity()
            break

        else:
            date = input("Do you want the weather for today or tomorrow?\n")


def owm():
    while True:
        try:
            zipcode_1 = input("What is the zipcode?\n")
            link = "https://api.openweathermap.org/data/2.5/weather?zip=" + zipcode_1 + ",US&appid=9ab510de1e35325e954f7a1079ee3ba0"
            weather_data = requests.get(link).json()
            Max_temp = weather_data['main'].get("temp_max")
            Min_temp = weather_data['main'].get("temp_min")
            humidity = weather_data['main'].get("humidity")
            for item in weather_data['weather']:
                print("Today's weather status: " + item['main'])
            weather = item['main']
            if weather.lower() == 'rain':
                print("Be sure to bring an umbrella, it is going to rain.")
            print("Maximum Temperature: " + str(Max_temp))
            print("Minimum Temperature: " + str(Min_temp))
            print("Humidity: " + str(humidity))
            break#Use break when there are codes afterwards

        except KeyError:
            print("Wrong input. Do it again!")

while choice != 'pyowm' or "owm": #how to use while loop here
    if choice == "pyowm":
        p_y_owm()
        break
    if choice == "owm":
        owm()
        break
    else:
        choice = input("Do you want to run pyowm or owm?\n").lower()

