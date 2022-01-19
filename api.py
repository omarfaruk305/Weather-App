import json
import requests
import time
from datetime import datetime

class Weather:
    def __init__(self):
        self.api_url = 'https://api.openweathermap.org'
        self.api = '4066d02659709f62c380ebe1628d8b42'

    def get_weather(self, city):
        try:
            response = requests.get(
            self.api_url+'/data/2.5/weather?q='+city+'&&appid='+self.api).json()

            city_name = response['name']
            country = response['sys']['country']
            temp = int(response['main']['temp']-273.15)
            description = response['weather'][0]['description']
            icon = response['weather'][0]['icon']
            utc_time_Unix=response["dt"] #Current time, Unix, UTC.Unix time forms,localtimes derived from these
            localtime_dt=response["timezone"]#UTC +- ,Shift in seconds from UTC
            local_time=int(utc_time_Unix)+int(localtime_dt)
            date_time=str(datetime.utcfromtimestamp(local_time).strftime('%Y-%m-%d at %H:%M:%S'))#converts Unix to datestime
            
            information=[city_name,country,temp,description,icon,date_time]
            return information

        except Exception as e:    #some conflicts when same city name is already exist in other countries.exp. Breda(IT,NL)
            return("-")


info = Weather()
# print(info.get_weather("Situering"))