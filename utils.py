CODE_TO_SMILE = {
    "Clear": "Ясно \U00002600",
    "Clouds": "Хмарно \U00002601",
    "Rain": "Дощ \U00002614",
    "Drizzle": "Дощ \U00002614",
    "Thunderstorm": "Гроза \U000026A1",
    "Snow": "Cніг \U0001F328",
    "Mist": "Туман \U0001F32B"
}

def get_weather_emoji(weather_description):
    return CODE_TO_SMILE.get(weather_description, "Подивися у вікно, не зрозумію, що там за погода!")

