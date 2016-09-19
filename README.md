#**Floodtags Social Network Analysis**

This repository contains the scripts required for performing a basic Social Network Analysis and influencer analysis on Floodtags data. The files contained do the following:

* SNA_execute: The main launch file. Launch from terminal with python SNA_execute.py <starting_date> <ending_date> <database>. Format for the dates is: YYYY-MM-DD

* SNA_script: Contains the logic of the Social Network Analysis and feature calculations

* api_request: Contains the logic to request data from the Floodtags API and restructure it for further processing

* mentions_to_edgelist: Contains the logic to convert dataset from raw tweets to a directed graph edge list based on @mentions, required for SNA

* csv files: Example output files, in total four csv files are generated

Installation:

1. Create Virtual Environment on a Server
2. Install dependencies with `pip install -r requirements.txt`
3. Run file in directory using `python SNA_execute.py <starting_date> <ending_date> <database>`
4. 4 .csv files will be created in the directory containing the top 50 of each of four user statistics

in-degree: the number of times a user is mentioned by other users
out-degree: the number of times a user has mentioned other users
page-rank: the degree by which a user was mentioned by other users, placing more weight on mentions from other high ranked users
betweenness centrality: the relative importance of a user in the network in terms of reach. Without these users there is no communication. 