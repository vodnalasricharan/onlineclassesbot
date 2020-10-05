import os
class Config(object):
	BOT_TOKEN = os.environ.get('BOT_TOKEN')
	USERNAME = os.environ.get('USERNAME')
	PASSWORD = os.environ.get('PASSWORD')
	#comment above 3 lines
	#If above lines wont work then use below and pass credentials
	#uncomment below 3 lines
	# BOT_TOKEN = os.environ.get('BOT_TOKEN','TELEGRAM_BOT_API_TOKEN')
	# USERNAME = os.environ.get('USERNAME','MAIL_ID')
	# PASSWORD = os.environ.get('PASSWORD','MAIL_PASSWORD')
