import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="om0AvElOnmtjAmBmjUmkg"
consumer_secret="ctVq0hN3zYyc90t6ZX7LidAp9RkNeqAwPOrWaPuteE"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token="241596263-34CuJsLeexQOZlWMPkwJXjEEU0Ij9Z4ALUN9gRqG"
access_token_secret="fpJ1egXcGfq2gdiwM1GebRCQOA5eh4lr9XOO416eOo"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print api.me().name

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's 
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
api.update_status('Updating using OAuth authentication via Tweepy!')
