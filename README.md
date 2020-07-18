# YouTube Covid Metrics
## Description
Obtain and store data of top YouTube videos and compare average metrics to COVID-19 related videos.
## Brief (fictional client)
Client demands for software that can obtain metrics of video engagement and performance in a certain time period. COVID-19 related videos should be identified through certain keywords/topics established in the video data obtained.
These specific metrics are required for analysis:
- Average views
- Average COVID-19 views
- Average comments per view
- Average COVID-19 comments per view 
- Average likes/dislikes per view
- Average COVID019 likes/dislikes per view

Data should be exported in a format where an excel file can be used to illustrate trends. This practice is important as the data needs to be human-readable and used for futher analysis.
## Setup
#### Libraries
Google APIs Client
#### Pip
1. pip install --upgrade google-api-python-client
2. pip install --upgrade google-auth-oauthlib google-auth-httplib2
#### Note (important)
Download YOUR_CLIENT_SECRET_FILE.json and place in directory, this is done following the api setup tutorial provided by Google.
#### Running
1. Run **grab_data.py**.
2. Run **transform_data.py**.
3. Run **analyse_data.py**.
## Report
The goal of this project is to be able to visualise how videos with a title containing COVID-19/coronavirus perform against the other popular videos.
**grab_data.py** utilises YouTube v3 API. This script is designed to iterate through all possible pages that are returned by Google as to exhuast all data. The main directory for all data is simply called data however, the subdirectories are named after the day, month and year. This implementation allows for separation of data by a difference of a day - this script should be ran every day to harvest more data.

**transform_data.py** is designed to iterate through each subdirectory that contains the data. This script then transforms the data into a format (list of dictionaries) that is easily programmable. The list is then saved as a pickle file in the respective subdirectory, this storage allows for other usage.

**analyse_data.py** reads the generated pickle files and creates a list of videos. This list then iterated through to obtain desired statistics for further calculations. This script only considers the title as a source of identifying COVID-19 related videos because some channels use descriptions and tags with unrelated information. If the title contains the virus then the video will be almost always COVID-19 related.

The original metrics measured against views but later through development it was decided that comparing engangement (comments, likes and dislikes) together seemed more conclusive. However, engagement per view is still considered.
## Author
Alex Sikorski
