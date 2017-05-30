# -*- coding: utf-8 -*-

import twitter
import time 

from config import *
from calc import temperature
from dateutil.parser import parse

#ClimateChangeBt user id
id = 867817641439842304
full_name = "ClimateChangeBt"

api = twitter.Api(consumer_key,
		  consumer_secret,
		  access_token_key,
		  access_token_secret)

list = api.GetUserTimeline(user_id=id, screen_name=full_name, include_rts = False)

def sendTweet():
   stri = "Currently, the long-term climate of planet earth is approximately " + str(temperature()).replace(".",",") + "°C warmer than it was on average from 1880-1920."
   print "Sending: " + stri
   api.PostUpdate(stri)
   print "Sleeping for 4 hours..."
   time.sleep(4*60*60)

#Checks at start if last tweet is older than 4 hours
if len(list) > 0:
    last_tw_time = list[0].created_at
    tupl = parse(last_tw_time)
    ti = time.time()-time.mktime(tupl.timetuple())
    if ti < (4*60*60):
        restTime = time.mktime(tupl.timetuple()) + 4 * 60 * 60 - time.time()
        print "Sleeping for " + str(restTime) + " seconds..."
        time.sleep(restTime)

while 1:
    sendTweet()
