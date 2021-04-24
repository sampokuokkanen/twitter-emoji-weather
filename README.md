# Twitter automatic name changer based on current weather

Example-

My twitter handle @KuokkanenSampo

<img src="https://github.com/raghavkhanna30/twitter-auto-name-changer/blob/master/upload/Capture3.PNG">

Inspired by the project 



This bot will automatically change your name based the current weather in your location followers (Written in Python)

## Usage

## Step 0

Create a virtual env
`python3 -m venv env`
Then activate it:
`source env/bin/activate`
Install tweepy:
`pip install -r requirements.txt`


## Step 1 - Getting twitter API keys

go to the twitter developers page. 
In the Create an app enter the informations like app name, app description and so on. it asked me to clearly explain the reason of how I'm going to use the app
After reviewing the terms, app will be created. 
Note down the Consumer API key, Consumer API Secret key and Access token & access token secret keys!

## Step 2 - updating config.py

in config.py enter your Consumer API key, Consumer API Secret key and Access token & access token secret keys.
after that save it.

  In mainbot.py Edit your username and you are all done!
  
 ## Heroku deployment
 
 for this you need to create a procfile with worker as mainbot.py and that's it!
 
 

 
 
