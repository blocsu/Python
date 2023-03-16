from json import load
from urllib.request import urlopen
date = load(urlopen('https://www.cbr-xml-daily.ru/daily_json.js'))
print(date['Valute']['USD']['Value'])