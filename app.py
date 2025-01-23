"""

Author: Er. Amar kumar
Professional: Senior Software Enginner


===================================================

Library used in this project

1. Time 
2. Request 
3. Beautiful Soup(bs4)
4. plyer

"""

import time 
import requests 
import bs4
from plyer import notification



# function to get weather information 

def getWeatherInfo(url):
    try:
       response = requests.get(url)
       return response.text
    except Exception:
       print(f"Unable to fetch weather updates from {url}")


WEATHER_API_ENDPOINT = "Your wather api end point"


htmlData = getWeatherInfo(WEATHER_API_ENDPOINT)



soup = bs4.BeautifulSoup(htmlData,'html.parser')


tempature = soup.find_all("span", class_=" _-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY") 
rain_predition = soup.find_all("span", class_=" _-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf") 


tempature = (str(tempature))
rain_predition = str(rain_predition)

description = f"Temperature  {tempature[128:-9]}  In Antri, Gwalior, Madhya Pradesh  \n   Precipitation: {rain_predition[131:-14]}"


notification.notify(
        title="Live Wwather Report",
        message=description,
        app_name="Weather App",
        timeout=10
    )

