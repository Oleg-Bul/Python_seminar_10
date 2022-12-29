import requests
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
print(data['Valute']['EUR']['Name']), print(data['Valute']['EUR']['Value'])
print(data['Valute']['USD']['Name']), print(data['Valute']['USD']['Value'])
