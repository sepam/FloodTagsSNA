# **FloodTags Social Network Analysis**

This repository contains the scripts required for performing a basic Social Network Analysis and influencer analysis on FloodTags data. The entire analysis can be run from a single command line command, but the individual scripts can also be used independently and tied into existing workflows. The files contained do the following:

* **SNA_execute**: The main launch file. Launch from terminal with python SNA_execute.py <starting_date> <ending_date> <database>. Format for the dates is: YYYY-MM-DD. This will run all three major scripts in turn through a single command line.

* **api_request**: Contains the logic to request data from the Floodtags API and restructure it for further processing. Outputs a pandas dataframe as csv. 

* **mentions_to_edgelist**: Contains the logic to convert dataset from raw tweets to a directed graph edge list based on @mentions, required for SNA. Outputs edge list as csv.

* **SNA_script**: Contains the logic of the Social Network Analysis and feature calculations. Outputs 4 csv files with the top 50 users in each category.

* **csv files**: Example output files of the SNA script based on real FloodTags data.

### **Installation**:

1. Create Virtual Environment on server
2. Install dependencies with `pip install -r requirements.txt`
3. Run file in directory using `python SNA_execute.py <starting_date> <ending_date> <database>`. The arguments are mandatory, no defaults are provided. Format for the dates is: YYYY-MM-DD.
4. All .csv files will be created in the directory containing the top 50 of each of four user statistics

### **Interpretation of results**

**in-degree**: the number of times a user is mentioned by other users

**out-degree**: the number of times a user has mentioned other users

**page-rank**: the degree by which a user was mentioned by other users, placing more weight on mentions from other high ranked users

**betweenness centrality**: the relative importance of a user in the network in terms of reach. Without these users there is no communication. 

### **Further considerations**

* Results are better over larger data sets.

* It is recommended to perform this analysis at the following times: once a month, once a week during rainy season, and after every major flood event.