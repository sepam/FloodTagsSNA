# script that automates all steps
import requests
import json
import api_request
import mentions_to_edgelist
import SNA_script
import time
import datetime


time_of_request = str(datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")) + '.000Z'

# possibilities for database are:
# "indonesia", "fews-world", "flood", "philippines",
# "philippines-english-precise", "philippines-english-recall", "poland"

start_time = "2016-09-10T17:00:00.000Z"
end_time = time_of_request
# end_time = "2016-09-15T17:00:00.000Z"
database = "indonesia"
water_depth = "false"
locations = "false"


def full_request(start_time=start_time, end_time=end_time, database=database, water_depth=water_depth, locations=locations):
    start = time.time()
    pd_tweets = api_request.FloodTagsAPI_refined_tweets(
        rq_database=database,
        rq_until=end_time,
        rq_since=start_time,
        rq_hasWaterdepth=water_depth,
        rq_hasLocations=locations)
    mentions_to_edgelist.convert_to_edgelist(pd_tweets)
    influencers = SNA_script.generate_influencers()

    print(influencers)
    print('It took', time.time()-start, 'seconds to complete this analysis.')

def request_metadata(
        start_time=start_time,
        end_time=end_time,
        database=database,
        water_depth=water_depth,
        locations=locations):
    start = time.time()
    def get_request(
            rq_skip=0,
            rq_limit=1,
            rq_database=database,
            rq_until=end_time,
            rq_since=start_time,
            rq_hasWaterdepth=water_depth,
            rq_hasLocations=locations
            ):

        # the amount of tags to skip from the beginning
        # the amount of tags to return
        rq_base_url_start = "https://api.floodtags.com/v1/tags/"
        rq_base_url_end = "/index"
        # rq_database = location
        # rq_until = "2016-09-04T17:00:00.000Z"
        # rq_since = "2016-09-03T17:00:00.000Z"
        # rq_hasWaterdepth = "false"
        # rq_hasLocations = "false"
        # rq_limit
        # location
        rq_url = rq_base_url_start \
                 + rq_database \
                 + rq_base_url_end \
                 + "?until=" + rq_until \
                 + "&since=" + rq_since \
                 + "&hasWaterdepth=" + rq_hasWaterdepth \
                 + "&hasLocations=" + rq_hasLocations \
                 + "&skip=" + str(rq_skip) \
                 + "&limit=" + str(rq_limit)

        r = requests.get(rq_url)
        r_json = json.loads(r.text)
        return r_json

    data = get_request()
    print('tweets between', start_time, 'and', end_time)
    print('number of tweets: ', data['meta']['total'])
    print('server time to process: ', data['meta']['processTime'])
    print('total time for request call to finish: ', time.time() - start)
