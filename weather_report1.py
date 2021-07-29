import pyowm
from pyzipcode import ZipCodeDatabase

#ask for user input
User_zipcode = input("What is your zipcode?\n")
#convert zipcode into city name
zcdb = ZipCodeDatabase()
zipcode = zcdb[User_zipcode].city
print(zipcode)

owm = pyowm.OWM('9ab510de1e35325e954f7a1079ee3ba0')
mgr = owm.weather_manager()
location = mgr.weather_at_place(zipcode)
weather = location.weather

print(weather.status)

temp = weather.temperature('celsius')
for key, value in temp.items():
    print(key, value)

humid = weather.humidity
print(humid)
