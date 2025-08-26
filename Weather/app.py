import requests

api_key = "ba13c721b70c12151bdde7ff7e617d8c"


user_input = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
        
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°F")


