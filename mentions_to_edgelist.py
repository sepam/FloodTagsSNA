# process the tweet lists to find out who mentions who
import pandas as pd


def convert_to_edgelist(pd_tweets):
    # read the file that was stored
    # pd_tweets = pd.read_csv("tweets_dataframe.csv")
    pd_tweets = pd_tweets

    # create a column which include the found mentions in a tweet for each tweet
    pd_tweets['mentions'] = pd_tweets['tweet'].str.findall('(?<=^|(?<=[^a-zA-Z0-9-\.]))@([A-Za-z_]+[A-Za-z0-9_]+)')

    # selects tweets with only mentions in them
    all_mentions = pd_tweets[(pd_tweets['mentions'].str.len() > 0)]
    all_mentions = all_mentions.reset_index()

    # create edge list
    edge_list = pd.DataFrame()
    for i in range(len(all_mentions)):
        for j in range(len(all_mentions.ix[i]['mentions'])):
            edge_pair = pd.DataFrame([[all_mentions.ix[i]['username'],
                                       all_mentions.ix[i]['mentions'][j]]], columns=["source", "target"])
            edge_list = edge_list.append(edge_pair)

    # save the dataframe to csv
    edge_list.to_csv("temp/edge_list.csv", index=False)

    return print("Edge list created and saved as csv...")


# Notes and various functions:
# DataFrame.ix[] lets you specify the row and column values you want. you can include slicing here
# return the number of mentions in the specified tweet
# len(pd_tweets.ix[1, ["mentions"]][0])
# return only tweets with mentions in them
# pd_tweets[(pd_tweets["tweet"].str.contains('(?<=^|(?<=[^a-zA-Z0-9-\.]))@([A-Za-z_]+[A-Za-z0-9_]+)'))]
# conditional selection in a pandas dataframe
# foo = df.ix[(df['column1']==value) | (df['columns2'] == 'b') & (df['column3'] == 'c']
# regular expression that matches words starting with an "@" but disregards emails, it also allows for usernames
# with underscores in them like @basuki_btp
# (?<=^|(?<=[^a-zA-Z0-9-\.]))@([A-Za-z_]+[A-Za-z0-9_]+)
