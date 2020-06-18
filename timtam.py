import tweepy
import time
import cred
from datetime import date


# Sets to wait a day
def tweet_tam():
    # Set wait time
    interval = 60 * 60 * 24
    # Set auth
    auth = tweepy.OAuthHandler(cred.consumer_key, cred.consumer_secret)
    auth.set_access_token(cred.access_token, cred.access_token_secret)
    api = tweepy.API(auth)

    # While loop to run indefinitely
    while True:
        # Check the time passed from timtam creation
        today = date.today()
        tim_date = date(1964, 2, 16)
        months = check_month_plural(today.month - tim_date.month)
        years = today.year - tim_date.year
        days = check_day_plural(today.day - tim_date.day)
        str = 'The British people have gone {years} years, {months} and {days} without reasonably priced TimTams. #BorisJohnson'.format(years, months, days)
        api.update_status(str)
        # this sleep operation takes the INTERVAL variable and sleeps for  #24hrs
        time.sleep(interval)


# Check if plural or not
def check_month_plural(time_passed):
    return "{} {}".format(time_passed, 'month' if time_passed == 1 else 'months')


# Check if plural or not
def check_day_plural(time_passed):
    return "{} {}".format(time_passed, 'day' if time_passed == 1 else 'days')


if __name__ == "__main__":
    tweet_tam()
