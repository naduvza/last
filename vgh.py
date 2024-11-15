from bs4 import BeautifulSoup
import requests

url_weather = "https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%85%D0%BC%D0%B5%D0%BB%D1%8C%D0%BD%D0%B8%D1%86%D1%8C%D0%BA%D0%B8%D0%B9"
response_weather = requests.get(url_weather)
if response_weather.status_code == 200:
    soup_weather = BeautifulSoup(response_weather.text, features="html.parser")
    temp = soup_weather.find("p", class_="today-temp").text.strip()
    print("Температура в Хмельницькому:", temp)
