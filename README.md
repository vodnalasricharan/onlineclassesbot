
# ONLINE CLASSES BOT

Online Classes Bot is a telegram bot which can be deployed to a server, heroku or on your local machine. It can attend your Google Meet and Zoom classes for you.

## Bot Commands

    /meet - Command to join Google Meet classes or metting
    /gchat - To send messages in Google meeting
    /zoom - Command to join Zoom Meeting
    /status - Sends screenshot of the web page
    /exitmeet - Exit Google meeting
    /loginteams - To login to teams
    /jointeams - To join meeting in teams
    /exitteams - To exit meeting in teams
    /restart - Close all the opened window and restarts the script
## Usage
	
	Join Google Meeting
    /meet https://meet.google.com/agr-ghts-ade
    
    send messages in Gmeet
    /gchat yourmessage
    
    Join Zoom Meeting
    /zoom 12354674654 ax56rR
	
    Get screenshot of the web page
    /status
    
    Exit the ongoing Googlemeeting
    /exitmeet
    
    To login Microsoft teams
    /loginteams
    
    To join meeting in Microsoft teams
    /jointeams channel_name_to_join
    
    Exit meeting in Teams
    /exitteams

    Close all the opened window and restarts the script
    /restart

## Deploy to Local Machine and Server

> Set ENVIRONMENT VARIABLES according to VARIABLES in [config.py](https://github.com/vodnalasricharan/onlineclassesbot/blob/master/config.py)



	
 1. Download and Install Google Chrome and Chromedriver.
 2. `git clone https://github.com/vodnalasricharan/onlineclassesbot`
 3. `cd onlineclassesbot`
 4. `pip install -r requirements.txt`
 5. `python chromium.py` 

## Deploy to Heroku
**One Click Deploy**

> Note: In one click deploy you will have to re-login every day.


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/vodnalasricharan/onlineclassesbot)


**Conventional Deploy**

> Note: Login to your Google account from your local machine first, so that you don't have to re-login again and again on Heroku.


> Set ENVIRONMENT VARIABLES according to VARIABLES in [config.py](https://github.com/vodnalasricharan/onlineclassesbot/blob/master/config.py)



1. Download and Install Google Chrome and Chromedriver.
 2. `git clone https://github.com/vodnalasricharan/onlineclassesbot`
 3. `cd onlineclassesbot`
 4. `pip install -r requirements.txt`
 5. `python chromium.py`
 6. Login to your Google Account.
 7. Now through Heroku-CLI login to your Heroku account
 8. Create a Heroku App `heroku create appname --buildpack heroku/python`
 9. Set Chromedriver Builpack `heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver -a appname`
 10. Set Google Chrome buildpack `heroku buildpacks:add https://github.com/1337w0rm/heroku-buildpack-google-chrome -a appname`
 11. Initialize git repository  `git init`
 12. Select this app in your Heroku-CLI `heroku git:remote -a appname`
 13. Commit the changes `git commit -am "Your commit message"`
 14. Push Code to Heroku `git push heroku master`
 15. Scale the dynos `heroku ps:scale worker=1`
 
