import pyowm

owm = pyowm.OWM('91c713db144e1ce5a94dffd4229169ed',language='ru')

city = input('Погоду в каком городе Вы хотите узнать:').title()
observation = owm.weather_at_place(city)
w = observation.get_weather()
print(w)
tempe = w.get_temperature('celsius')['temp']
print('В указанном городе', tempe, 'градусов по Цельсию')
