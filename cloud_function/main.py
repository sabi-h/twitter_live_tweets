import os
import tweepy as tw
import pandas as pd

from dotenv import load_dotenv, find_dotenv


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


api_key = os.environ.get('api_key')
api_secret_key = os.environ.get('api_secret_key')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')


auth = tw.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


HASHTAG = '#london'
NO_OF_TWEETS = 30
BUCKET = 'twitter_tweets_data'


def get_tweets(hashtag, no_of_tweets):
    """
    Returns:
        List of tuples where each tuple contains:
        - creation date
        - auther screen name
        - text

    """
    tweets = tw.Cursor(api.search, q=HASHTAG, lang='en', result_type='recent').items(NO_OF_TWEETS)
    return [(tweet.created_at, tweet.author.screen_name, tweet.text) for tweet in tweets]



def main(request):
    """

    Writes (overwrites if already exists) csv file in 
    Google cloud storage with naming format:
        gs://bucket/[HASHTAG]_recent_tweets.csv

    Args:
        request (flask.Request): HTTP request object.

    Returns:
        None

    """
    # return 'WHAT??'

    # Future: Get hashtag from request
    hashtag = HASHTAG

    data = get_tweets(hashtag=hashtag, no_of_tweets=NO_OF_TWEETS)

    columns = ['created_at', 'author_screen_name', 'text']
    df = pd.DataFrame(data, columns=columns)
    df['hashtag'] = hashtag

    df.to_csv(f'gs://{BUCKET}/recent_tweets.csv', index=False)



if __name__ == '__main__':
    result = main(request='')




























