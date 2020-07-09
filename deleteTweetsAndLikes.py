import tweepy
import logging
from config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def deleteAllTweets(api):
    try:
        for tweet in tweepy.Cursor(api.user_timeline).items():
            print(tweet.text)
            api.destroy_status(tweet.id)
    except Exception as e:
        logger.error('Error while deleting retweets', exc_info=True)

def deleteAllLikes(api):
    try:
        for tweet in api.favorites():
            print(tweet.text)
            api.destroy_favorite(tweet.id)
    except Exception as e:
        logger.error('Error while deleting retweets', exc_info=True)

def main():
    api = create_api()
    deleteAllTweets(api)
    logger.info('Deleted all retweets')
    deleteAllLikes(api)
    logger.info('Deleted all likes')
if __name__ == "__main__":
    main()
    