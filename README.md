# Twitter Emoji Weather

Example-

My twitter handle @KuokkanenSampo

<img src="https://github.com/sampokuokkanen/weather-in-twitter-name/blob/master/upload/profile.png">

Inspired by the project [Twitter automatic name changer based on your followers](https://github.com/raghavkhanna30/twitter-auto-name-changer), and indeed most of the source is also identical. So thanks for [Raghav Khanna](https://twitter.com/erRaghavKhanna) for the original project!


This bot will automatically change your name based the current weather in your location followers (Written in Python) once in 15 minutes. It fetches the current weather using the OpenWeather API. 

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
Add permission to do post requests to the app. 
Note down the Consumer API key, Consumer API Secret key and access token, access token secret, username, and OpenWeather API keys!

## Step 2 - updating config.py

in config.py enter your Consumer API key, Consumer API Secret key and Access token & access token secret keys.
after that save it.

  In mainbot.py Edit your username and you are all done!
  
 ## Heroku deployment
 
 for this you need to create a Procfile with worker as mainbot.py and that's it! There is a sample one in this repository which you can use. 
 
 

 
 
