# from https://chimpler.wordpress.com/2013/03/13/using-the-mahout-naive-bayes-classifier-to-automatically-classify-twitter-messages/
# how to use it 
# cd /Users/roberto/workspace/python/tweepy
# python scripts/twitter_fetcher.py > tweets-train-<termino>.txt
import tweepy
import sys

CONSUMER_KEY='om0AvElOnmtjAmBmjUmkg'
CONSUMER_SECRET='ctVq0hN3zYyc90t6ZX7LidAp9RkNeqAwPOrWaPuteE'
ACCESS_TOKEN_KEY='241596263-34CuJsLeexQOZlWMPkwJXjEEU0Ij9Z4ALUN9gRqG'
ACCESS_TOKEN_SECRET='fpJ1egXcGfq2gdiwM1GebRCQOA5eh4lr9XOO416eOo'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

pageCount = 5
#if len(sys.argv) >= 2:
#	pageCount = int(sys.argv[1])
hashtags = ['"estoy buscando" OR busco OR "he buscado"']

for tag in hashtags:
	maxId = 999999999999999999999
	for i in range(1, pageCount + 1):
		results = api.search(q='#%s' % tag, max_id=maxId, count=100)
		#print len(results)
		for result in results:
			maxId = min(maxId, result.id)
			#print "%s\t%s" % (result.id, result.text.encode('utf-8').replace('\n', ' '))
			print "%s" % (result.text.encode('utf-8').replace('\n', ' '))
