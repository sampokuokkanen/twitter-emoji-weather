import tweepy
import logging
import os
from config import create_api, get_weather
import time
import pytemperature

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def current_emoji(user):
    # update string split if you don't use this naming format for twitter profile:
    # 'insert_your_name|{weather_icon(user)} Followers'
    current_emoji = user.name.replace('|', ' ').split()
    return current_emoji[-1]


def weather_icon(main, description, prev_weather):
    weather_types = {
        "Rain": "🌧️", "Thunderstorm": "⛈️", "Drizzle": "🌦️", "Snow": "🌨️",
        "Clear": "🌞"
    }
    if (prev_weather in ["🌧️", "⛈️", "🌦️"]) and (main == "Clear"):
        return "🌈"
    elif "few clouds" in description:
        return "⛅"
    elif "scattered clouds" in description:
        return "🌥️"
    elif main in weather_types:
        return weather_types[main]
    else:
        return "🌫️"


def main():
    while True:
        api = create_api()
        username = os.getenv('TWITTER_USERNAME')
        user = api.get_user(username)
        city = os.getenv('CITY')
        weather = get_weather(city)
        current_temp = pytemperature.k2c(weather["main"]["temp"])
        old_emoji = current_emoji(user)
        icon = weather_icon(weather["weather"][0]["main"], weather["weather"][0]["description"], old_emoji)
        logger.info(
            f'The old weather icon vs the old one: {old_emoji} -> {icon}')
        # Update weather icon and temperature into twitter profile
        api.update_profile(
            name=f'Sampo Kuokkanen | {round(current_temp)}° in {city} | {icon}')

        logger.info("Waiting to refresh..")
        time.sleep(900)


if __name__ == "__main__":
    main()
