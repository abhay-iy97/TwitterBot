# Twitter Bot

Following the tutorial [here](https://realpython.com/twitter-bot-python-tweepy/#presenting-the-example-bots).
## [config.py](https://github.com/abhay-iy97/twitter-bot/blob/master/config.py)

- Creates the basic configuration required to access the Twitter API via Tweepy.
- Does the authentication using the Consumer API keys and the Access tokens which can be generated [here](developer.twitter.com).

[keys/keys.txt](https://github.com/abhay-iy97/twitter-bot/blob/master/config.py#L7) structure:
```
API key:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   
API secret key:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   
Access token:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   
Access token secret:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   
```
## [deleteTweetsAndLikes](https://github.com/abhay-iy97/twitter-bot/blob/master/deleteTweetsAndLikes.py)
- Script to delete all tweets and likes.

## [follower_bot](https://github.com/abhay-iy97/twitter-bot/blob/master/follower_bot.ipynb)
- A bot to follow all your followers.

## [favAndRetweet_bot](https://github.com/abhay-iy97/twitter-bot/blob/master/favAndRetweet_bot.ipynb)
- Bot to like all tweets in the current stream which match a certain filter.
- Retweet all tweets in the current stream which match a certain filter.
