import json
import requests

class Weather:
    def __init__(self):
        self.api_url='https://api.openweathermap.org'
        self.api='4066d02659709f62c380ebe1628d8b42'

    def get_weather(self,city):
        try:
            response=requests.get(self.api_url+'/data/2.5/weather?q='+city+'&&appid='+self.api).json()
      
       
            city_name=response['name']
            country=response['sys']['country']
            temp=int(response['main']['temp']-273.15)
            description=response['weather'][0]['description']
            icon=response['weather'][0]['icon']
            information=[city_name,country,temp,description,icon] #here ,we need ordered information,sozluk olursa karisik sira
            return information
           

        except Exception as e:
            return("Please enter a valid city")


        

info=Weather()
print(info.get_weather('New York City'))
    