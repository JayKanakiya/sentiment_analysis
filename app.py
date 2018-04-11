import tweepy
import csv
from textblob import TextBlob

# Auth
consumer_key = "CONSUMER KEY"
consumer_secret = "CONSUMER SECRET"
access_token = "ACCESS TOKEN"
access_token_secret = "ACCESS TOKEN SECRET"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

app = tweepy.API(auth)

# Input Tag
tag = input("Enter Tag: ")
tweets = app.search(tag)

# Opening CSV file
file = open('sentiment.csv','w')
writer = csv.writer(file)

for t in tweets:
	text1 = t.text.encode('utf-8').strip()
	# Storing Sentiment
	analysis  = TextBlob(t.text).sentiment
	sentiment = analysis.polarity
	# Emotions based on sentiment
	if sentiment>0:
		writer.writerow([text1,"Positive",sentiment])
	elif sentiment==0:
		writer.writerow([text1,"Neutral",sentiment])	
	else:
		writer.writerow([text1,"Negative",sentiment])

file.close()

