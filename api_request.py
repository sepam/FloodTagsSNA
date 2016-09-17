import requests
import json
import pandas as pd

# def FloodTagsAPI_estimated_time_for_request(rq_until="2016-09-06T17:00:00.000Z", rq_since="2016-09-04T17:00:00.000Z"):
#     data = FloodTagsAPI_refined_tweets(rq_limit=1, rq_until=rq_until, rq_since=rq_since)
#     total_tweets_in_time_period = data['meta']['total']
#     return(total_tweets_in_time_period)


def FloodTagsAPI_refined_tweets(
                rq_skip=0,
                rq_limit=100,
                rq_database="indonesia",
                rq_until="2016-09-06T17:00:00.000Z",
                rq_since="2016-09-04T17:00:00.000Z",
                rq_hasWaterdepth="false",
                rq_hasLocations="false"
                ):

    def get_request(
                rq_skip=rq_skip,
                rq_limit=rq_limit,
                rq_database=rq_database,
                rq_until=rq_until,
                rq_since=rq_since,
                rq_hasWaterdepth=rq_hasWaterdepth,
                rq_hasLocations=rq_hasLocations
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

    # TODO reformulate the parameter name > what does it actually take? in this case "data" are two different things for the functions below

    def request_total(data):
        total_tweets_in_time_period = data['meta']['total']
        return total_tweets_in_time_period

    def user_list(data):
        list_of_users = []
        for i in range(len(data)):
            list_of_users.append(data[i]['source']['username'])
        return list_of_users

    def tweet_list(data):
        list_of_tweets = []
        for i in range(len(data)):
            list_of_tweets.append(data[i]['text'])
        return list_of_tweets

    # get the total number of tweets in the specified period
    initial_query = get_request(rq_limit=1)
    total_number_tweets = request_total(initial_query)
    total_cycles = (total_number_tweets // 100) + 1

    # request the total user list in a specified period of time
    # TODO: I should get all the information in this request to minimize the amount of requests made. Therefore i have to write all data into memory, not just the userlist
    total_user_list = []
    total_tweet_list = []
    skip = 0
    for i in range(total_cycles):
        rq_limit = 100
        r_json = get_request(rq_skip=skip)
        tweets = r_json['tags']
        total_user_list = total_user_list + user_list(tweets)
        total_tweet_list = total_tweet_list + tweet_list(tweets)
        skip += rq_limit
        # time.sleep(1)

    # convert and merge the returned lists into a single pandas dataframe
    pd_tweets = pd.DataFrame()
    pd_tweets['username'] = total_user_list
    pd_tweets['tweet'] = total_tweet_list
    pd_tweets.to_csv('pandas.csv')


    return pd_tweets

# TODO: collect all the data into a pandas dataframe with the following information: twitter username, tweet, time of tweet, retweet yes/no

#
#print(FloodTagsAPI_refined_tweets())
# structure of tweets is:
# {'retweet': False,
# 'date': '2016-09-04T16:10:49.000Z',
# 'keywords': ['banjir'],
# 'id': 't-772466960437170178',
# 'source':
# {
# 'id': '772466960437170178',
# 'username': 'bewidha',
# 'userId': '69587534'},
# 'text': "setelah 'Hujan di Bulan Juni', perlu ada novel berjudul 'Banjir di Bulan Agustus'",
# 'waterDepth': -1,
# 'classes': [],
# 'photos': [],
# 'locations': [],
# 'urls': [],
# 'labels': []
# }