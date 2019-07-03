#!/usr/bin/env python

import subprocess
import sys
import praw
from praw.models import MoreComments
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

subreddit = str(sys.argv[1])
#subreddit = 'news'
#subreddit = 'the_donald'

reddit = praw.Reddit(user_agent="get mood of subreddit", client_id='', client_secret='')


#Bluemix Creds
#pi_username = ''
#pi_password = ''

#personality_insights = PersonalityInsights(username=pi_username, password=pi_username)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='',
    password='')

praw.models.reddit.subreddit.SubredditStream(subreddit)
#Get top 10 submissions and 25 newest? popular? comments
commentText = ""
print "Today's news: "
for submission in reddit.subreddit(subreddit).hot(limit=10):
	print(submission.title)
        print ""
	submission.comments.replace_more(limit=0)
	for top_level_comment in submission.comments:
		if isinstance(top_level_comment, MoreComments):
			continue
		commentText = commentText + " " + top_level_comment.body


response = natural_language_understanding.analyze(text=commentText, features=[features.Emotion(targets=['trump','donald'])])
data = (json.dumps(response, indent=1))

with open ('cashThesehands.json', 'w') as file:
   file.write(data)

from avgTheDonald import averageEmotions, publicEmotions
from calcYugeResults import generalEmotion, greatestEmotion
from yugePictures import sad, happy, disgust, angry, fear
#print results

trumpPerception = greatestEmotion()
dayPerception = generalEmotion()


print "The people in the " + subreddit + " subreddit feel " + dayPerception + "."
print "Mr. President, the people mostly feel " + trumpPerception + " towards you!"
if trumpPerception == 'anger':
    angry()
    print "YA FIRED"
elif trumpPerception == 'joy':
    happy()
    print "You deserve a vacation Mr. President!"
elif trumpPerception == 'disgust':
    disgust()
    print "THE LIBERAL MEDIA!!!"
elif trumpPerception == 'sadness':
    sad()
    print "SAD"
elif trumpPerception == 'fear':
    fear()
    print "Don't worry; we'll just take out a small loan"

