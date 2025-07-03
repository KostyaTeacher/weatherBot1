import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import F
from config import TOKEN, API_KEY
from utils import get_weather_emoji
import datetime
import requests


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: Message):
    await message.reply("Вітання! Напиши мені назву міста латиницею і я надішлю тобі прогноз погоди!\nНаприклад kyiv")


@dp.message(F.text)
async def get_weather(message: Message):
    try:
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={API_KEY}&units=metric")
        data = r.json()
        if data.get("cod") != 200:
            await message.reply("❌ Місто не знайдено. Перевірте правильність написання.")
            return

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]
        wd = get_weather_emoji(weather_description)

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunset_timestamp - sunrise_timestamp

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                            f"Погода у місті: {city}\nТемпература: {cur_weather}C° {wd}\n"
                            f"Вологість: {humidity}%\nТиск: {pressure} мм.рт.ст\nВітер: {wind} м/с\n"
                            f"Схід сонця: {sunrise_timestamp}\nЗахід сонця: {sunset_timestamp}\n"
                            f"Тривалість дня: {length_of_the_day}\n"
                            f"***Гарного дня!***")
    except requests.exceptions.RequestException as e:
        await message.reply("❌ Перевірте назву міста ❌")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
