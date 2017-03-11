import tweepy
from textblob import TextBlob

consumer_key = 'GXRGMp81R0PD9Pu7UDScNavwS'
consumer_secret = 'vUSGKt3HTIhGwYMqMTro1roWaa1yyOtM2GDEbZZdOJi5ecPEVA'

access_token = '205118755-FQUrcDELxcQefHK3MWU130B0KgjNACsOYLBWdSRE'
access_token_secret = 'Q6r53jDZM4SQw5nyaCPViylDJzbcqWWlpRf9oLfh76qbd'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	