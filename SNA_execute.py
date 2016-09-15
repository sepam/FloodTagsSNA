# script that automates all steps

import pandas as pd
import requests
import json
from api_request import FloodTagsAPI_refined_tweets
from mentions_to_edgelist import convert_to_edgelist
from SNA_script import generate_influencers

start_time = "2016-09-10T17:00:00.000Z"
end_time = "2016-09-15T17:00:00.000Z"
# possibilities for database are: "indonesia", <>
database = "indonesia"
water_depth = "false"
locations = "false"

pd_tweets = FloodTagsAPI_refined_tweets(rq_database=database,
                rq_until=end_time,
                rq_since=start_time,
                rq_hasWaterdepth = water_depth,
                rq_hasLocations = locations)
convert_to_edgelist(pd_tweets)
influencers = generate_influencers()

print(influencers)
