from internet_speed_tweet_bot import InternetSpeedBot

PROMISED_DOWN = 150
PROMISED_UP = 10
FIREFOX_DRIVER_PATH = "/home/walter/Public/drivers/firefox-driver/geckodriver"

bot = InternetSpeedBot(FIREFOX_DRIVER_PATH)
bot.get_internet_speed()
bot.tweeter_at_provider(promised_down=PROMISED_DOWN, promised_up=PROMISED_UP)