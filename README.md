
# ONLINE CLASSES BOT

Online Classes Bot is a telegram bot which can be deployed to a server, heroku or on your local machine. It can attend your Google Meet and Zoom classes for you.

## Bot Commands

    /meet - Command to join Google Meet classes or metting
    /zoom - Command to join Zoom Meeting
    /status - Sends screenshot of the web page
    /exitmeet - Exit Google meeting
    /restart - Close all the opened window and restarts the script
## Usage
	
	Join Google Meeting
    /meet https://meet.google.com/agr-ghts-ade
    
    Join Zoom Meeting
    /zoom 12354674654 ax56rR
	
    Get screenshot of the web page
    /status
    
    Exit the ongoing Googlemeeting
    /exitmeet

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

>Note: Add app url in main() function in chromium.py as mentioned in file

**Conventional Deploy**

> Note: Login to your Google account from your local machine first, so that you don't have to re-login again and again on Heroku.


> Set ENVIRONMENT VARIABLES according to VARIABLES in [config.py](https://github.com/vodnalasricharan/onlineclassesbot/blob/master/config.py)



1. Download and Install Google Chrome and Chromedriver.
 2. `git clone https://github.com/vodnalasricharan/onlineclassesbot`
 3. `cd onlineclassesbot`
 4. `pip install -r requirements.txt`
 5. `python chromium.py`
 6. Login to your Google Account.
 7. Before deploying comment `updater.start_pooling()` in `main()` function in chromium.py
 8. uncomment 
 	`updater.start_webhook(listen="0.0.0.0",
                           port=int(PORT),
                           url_path=str(Config.BOT_TOKEN))`
 	`updater.bot.setWebhook('heroku app link' + str(Config.BOT_TOKEN))`
>	note: add app link after deployement
 9. Now through Heroku-CLI login to your Heroku account
 10. Create a Heroku App `heroku create appname --buildpack heroku/python`
 11. Set Chromedriver Builpack `heroku buildpacks:add https://github.com/heroku/heroku-buildpack-chromedriver -a appname`
 12. Set Google Chrome buildpack `heroku buildpacks:add https://github.com/1337w0rm/heroku-buildpack-google-chrome -a appname`
 13. Initialize git repository  `git init`
 14. Select this app in your Heroku-CLI `heroku git:remote -a appname`
 15. Commit the changes `git commit -am "Your commit message"`
 16. Push Code to Heroku `git push heroku master`
 17. Scale the dynos `heroku ps:scale worker=1`
 
 ### Thanks Aditya,for this Idea😊.
 >This Bot is inspired from : https://github.com/1337w0rm/YeetMeet/
