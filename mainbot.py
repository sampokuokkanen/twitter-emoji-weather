import tweepy
import logging
from config import create_api, get_weather
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def current_emoji(user):
    # update string split if you don't use this naming format for twitter profile:
    # 'insert_your_name|{weather_icon(user)} Followers'
    current_emoji = user.name.replace('|', ' ').split()
    return current_emoji


def weather_icon(weather):
    weather_types = {
        "Rain": "🌧️", "Thunderstorm": "⛈️", "Drizzle": "🌦️", "Snow": "🌨️",
        "Clear": "🌈", "Clouds": "☁️"
    }
    if weather in weather_types:
        return weather_types[weather]
    else:
        return "🌫️"


def main():
    while True:
        # change to your own twitter_handle
        username = os.getenv('TWITTER_USERNAME')
        user = api.get_user('KuokkanenSampo')
        weather = get_weather()
        weather_icon = get_weather(weather)
        old_emoji = current_emoji(user)
        if old_emoji(user) == weather_icon:
            logger.info(
                f'You still have the same amount of followers, no update neccesary: {old_emoji} -> {weather_icon}')
        else:
            logger.info(
                f'Your amount of followers has changed, updating twitter profile: {old_emoji} -> {weather_icon}')
            # Updating your twitterprofile with your name including the amount of followers in emoji style
            api.update_profile(
                name=f'Sampo Kuokkanen | {weat}')

        logger.info("Waiting to refresh..")
        time.sleep(900)


if __name__ == "__main__":
    main()