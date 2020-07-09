import tweepy
import logging
logger = logging.getLogger()

#API Object
def create_api():
    f = open('keys//keys.txt', 'r')

    keys = dict()

    for i in f.read().split('\n')[:-1]: #-1 to avoid newline at end of the keys.txt
        try:
            keys[i.split(':')[0]] = i.split(':')[1]
        except:
            print("Error in accessing keys")

    auth = tweepy.OAuthHandler(keys['API key'], keys['API secret key'])
    auth.set_access_token(keys['Access token'], keys['Access token secret'])
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except:
        logger.error('Invalid credentials!', exc_info=True)
        raise e
    logger.info('API Created')
    return api