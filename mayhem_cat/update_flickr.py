#!/usr/bin/env python

import config
import sys
import os
import re
import json
import urllib2
import httplib

if sys.argv[1] == "mayhem":
    url = "http://api.flickr.com/services/rest/?&method=flickr.people.getPublicPhotos&api_key=%s&user_id=%s&format=json" % (config.FLICKR_API_KEY, config.FLICKR_USER)
    output_file = "mayhem_flickr_url"
else:
    url = "http://api.flickr.com/services/rest/?&method=flickr.photosets.getPhotos&api_key=%s&photoset_id=%s&format=json" % (config.FLICKR_API_KEY, config.FLICKR_HAIR_SET)
    output_file = "hair_set_url"

try:    
    response = urllib2.urlopen(url)
    jsonp = response.read()
    json_data = re.sub(r'([a-zA-Z_0-9\.]*\()|(\);?$)','',jsonp)
    data = json.loads(json_data)
    if sys.argv[1] == "mayhem":
        item = data['photos']['photo'][0]
    else:
        item = data['photoset']['photo'][0]
    purl = "http://farm%d.static.flickr.com/%s/%s_%s_b_d.jpg" % (item['farm'], item['server'], item['id'], item['secret'])
except urllib2.HTTPError, e:
    print "Could not fetch flickr image. HTTPError"
    sys.exit(1)
except urllib2.URLError, e:
    print "Could not fetch flickr image. URLError"
    sys.exit(1)
except httplib.HTTPException, e:
    print "Could not fetch flickr image. HTTPException"
    sys.exit(1)

if not os.path.exists(config.CACHE_DIR):
    os.makedirs(config.CACHE_DIR)

try:
    with open(os.path.join(config.CACHE_DIR, output_file), "w") as f:
        f.write(purl + "\n")
except IOError:
    print "IOError. :("
