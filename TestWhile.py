import pyowm

owm = pyowm.OWM(API_key='639cd74b40221a097d31bc5e64e343ab', language='ru')

forecast = input('Хотите получить прогноз погоды? (да или нет) \n').lower()

variants = ('д', 'l', 'd', 'y')

while forecast.startswith(variants):
    city = input('Какой город вас интересует? \n')

    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')['temp']

    print(f'В городе {city} сейчас {temperature} градусов по Цельсию.')
    print(f'Также в указанном городе {w.get_detailed_status()}.')

    forecast = input('Хотите получить еще один прогноз погоды? (да или нет) \n')

print('До свидания!')