#!/usr/bin/env python

import twitter
import config
import sys
import os

api = twitter.Api(consumer_key=config.CONSUMER_KEY,
                  consumer_secret=config.CONSUMER_SECRET, 
                  access_token_key=config.ACCESS_TOKEN_KEY, 
                  access_token_secret=config.ACCESS_TOKEN_SECRET)

statuses = api.GetUserTimeline("MayhemBCN")

if not os.path.exists(config.CACHE_DIR):
    os.makedirs(config.CACHE_DIR)

with open(os.path.join(config.CACHE_DIR, "twat"), "w") as f:
    f.write(statuses[0].text)
