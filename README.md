#### Most Recent #London Tweets
Cloud-based solution to showcase a stream of Twitter tweets that include the hashtag #london to end-users with refresh time of 1 minute.
[Link to Dashboard (DataStudio)](https://datastudio.google.com/s/vIU2tiJqnk4)


#### GCP Architecture
![GCP Architecture](architecture.png)

#### Setup (MacOS)
Instructions to setup this project in your local enviornment 


##### Clone the repository:
`git clone https://github.com/sabih-h/twitter_live_tweets.git`


##### Change to the directory:
`cd twitter_live_tweets`


##### Create virtual enviornment with python3:
`python3 -m venv venv`


##### Activate virtual enviornment:
`source venv/bin/activate`


##### Install Developer dependencies:
`python -m pip install -r requirements-dev.txt`


##### Change to the Cloud Function directory:
`cd twitter_live_tweets/cloud_function`


##### Create .env file and enter your twitter credentials:
```
api_key=[api_key]
api_secret_key=[api_secret_key]
access_token=[access_token]
access_token_secret=[access_token_secret]
```


##### Create .env.yaml file and enter your twitter credentials:
```
api_key: [api_key]
api_secret_key: [api_secret_key]
access_token: [access_token]
access_token_secret: [access_token_secret]
```


##### Deploy Cloud Function
`chmod +x deploy_function.sh; ./deploy_function.sh`





