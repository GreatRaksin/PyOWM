import pyowm
from colorama import init, Fore, Style
init()

owm = pyowm.OWM('639cd74b40221a097d31bc5e64e343ab', language='ru')
ans = input(Fore.CYAN + 'Вы хотите узнать погоду? (да или нет) \n' + Style.RESET_ALL).lower()

while ans.startswith(('д', 'l', 'd')):
    city = input('Введите город: \n')

    obs = owm.weather_at_place(city)
    w = obs.get_weather()
    temp = w.get_temperature('celsius')['temp']

    if temp > 5:
        print(f'В городе {city} сейчас {Fore.LIGHTRED_EX +  str(temp) + Style.RESET_ALL} градусов по Цельсию.')
    else:
        print(f'В городе {city} сейчас {Fore.LIGHTBLUE_EX + str(temp) + Style.RESET_ALL} градусов по Цельсию.')
    print(f'Также в указанном городе {w.get_detailed_status()}. \n')

    ans = input(Fore.CYAN + 'Вы хотите узнать погоду для другого города? (да или нет) \n' + Style.RESET_ALL).lower()

print('Всего доброго! 👋🏻')


