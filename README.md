**Floodtags Social Network Analysis
**
This repository contains the scripts required for performing a basic Social Network Analysis and influencer analysis on Floodtags data.

The files contained do the following:

`SNA_execute:` the main launch file. Launch from terminal with python SNA_execute <starting_date> <ending_date> <database>. Format for the dates is: YYYY-MM-DD
`SNA_script`: contains the logic of the Social Network Analysis and feature calculations
`api_request`: contains the logic to request data from the Floodtags API and restructure it for further processing
`mentions_to_edgelist`: contains the logic to convert dataset from raw tweets to a directed graph edge list based on @mentions, required for SNA
`csv files`: example output
