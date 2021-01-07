from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pause
import os
import logging
from telegram.ext import Updater, CommandHandler, run_async
from telegram import ChatAction
from config import Config
from os import execl
from sys import executable
import pickle

#Logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token = Config.BOT_TOKEN, use_context=True)
dp = updater.dispatcher


options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--disable-infobars")
options.add_argument("--window-size=1200,800")
options.add_argument("user-agent='User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'")
options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 1,
     "profile.default_content_setting_values.notifications": 1
  })

browser = webdriver.Chrome(options=options)
logged_in=False
teams_in=False

@run_async
def restart(update, context):
    restart_message = context.bot.send_message(chat_id=update.message.chat_id, text="Restarting, Please wait!")
    # Save restart message object in order to reply to it after restarting
    browser.quit()
    context.bot.send_message(chat_id=update.message.chat_id,text="Restarted Your Bot👍.")
    logging.info("restarting bot!!")
    with open('restart.pickle', 'wb') as status:
        pickle.dump(restart_message, status)
    execl(executable, executable, "chromium.py")
    
def status(update, context):
	try:
		browser.save_screenshot("ss.png")
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
		mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
		os.remove('ss.png')
		logging.info("*enquired status*")
		time.sleep(10)
		context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)

	except:
		context.bot.send_message(chat_id=update.message.chat_id, text="please /restart your bot🤖 to get status")
	
def zoom(update, context):
	logging.info("DOING")
	try:
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		
		usernameStr = Config.USERNAME
		passwordStr = Config.PASSWORD

		url_meet = update.message.text.split()[1]
		passStr = update.message.text.split()[2]

		if os.path.exists("zoom.pkl"):
			cookies = pickle.load(open("zoom.pkl", "rb"))
			browser.get('https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3Afad07e7074c3d678%2C10%3A1601127482%2C16%3A9619c3b16b4c5287%2Ca234368b2cab7ca310430ff80f5dd20b5a6a99a5b85681ce91ca34820cea05c6%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22d18871cbc2a3450c8c4114690c129bde%22%7D&response_type=code&flowName=GeneralOAuthFlow')
			for cookie in cookies:
				browser.add_cookie(cookie)
		else:
			browser.get('https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3Afad07e7074c3d678%2C10%3A1601127482%2C16%3A9619c3b16b4c5287%2Ca234368b2cab7ca310430ff80f5dd20b5a6a99a5b85681ce91ca34820cea05c6%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22d18871cbc2a3450c8c4114690c129bde%22%7D&response_type=code&flowName=GeneralOAuthFlow')
			username = browser.find_element_by_id('identifierId')
			username.send_keys(usernameStr)
			nextButton = browser.find_element_by_id('identifierNext')
			nextButton.click()
			time.sleep(7)

			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')

			password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
			password.send_keys(passwordStr)
			signInButton = browser.find_element_by_id('passwordNext')
			signInButton.click()
			time.sleep(7)


			browser.get('https://zoom.us/google_oauth_signin')
			time.sleep(7)

			if(browser.find_elements_by_xpath('//*[@id="authzenNext"]/div/button/div[2]')):
				context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
				context.bot.send_message(chat_id=update.message.chat_id, text="Need Verification. Please Verify")
				browser.find_element_by_xpath('//*[@id="authzenNext"]/div/button/div[2]').click()
				time.sleep(5)

				browser.save_screenshot("ss.png")
				context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
				mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
				os.remove('ss.png')
				time.sleep(20)

			pickle.dump( browser.get_cookies() , open("zoom.pkl","wb"))

			context.bot.send_message(chat_id=update.message.chat_id, text="Logged In!")

		browser.get('https://zoom.us/wc/join/'+ url_meet)

		time.sleep(5)
		browser.save_screenshot("ss.png")
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
		mid  = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), caption="Test", timeout = 120).message_id
		os.remove('ss.png')

		browser.find_element_by_xpath('//*[@id="joinBtn"]').click()
		time.sleep(5)
		browser.find_element_by_xpath('//*[@id="inputpasscode"]').send_keys(passStr)
		browser.find_element_by_xpath('//*[@id="joinBtn"]').click()

		time.sleep(10)

		context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)

		browser.save_screenshot("ss.png")
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
		mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
		os.remove('ss.png')

		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		context.bot.send_message(chat_id=update.message.chat_id, text="Attending you lecture. You can chill ")
		context.bot.send_message(chat_id=update.message.chat_id,text="To exit click /exitmeet ")
		pause
		logging.info("STAAAAPH!!")

	
	except:
		browser.quit()
		context.bot.send_message(chat_id=update.message.chat_id, text="Some error occurred retry!please /restart")

def meet(update,context):
	logging.info("logging in google account")
	try:
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		usernameStr = Config.USERNAME
		passwordStr = Config.PASSWORD
		url_meet = update.message.text.split()[-1]

		if os.path.exists("meet.pkl"):
			cookies = pickle.load(open("meet.pkl", "rb"))
			browser.get('https://accounts.google.com/')
			for cookie in cookies:
				browser.add_cookie(cookie)
		else:
			browser.get('https://accounts.google.com/')
			username = browser.find_element_by_id('identifierId')
			username.send_keys(usernameStr)
			nextButton = browser.find_element_by_id('identifierNext')
			nextButton.click()
			time.sleep(7)

			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')

			password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
			password.send_keys(passwordStr)
			signInButton = browser.find_element_by_id('passwordNext')
			signInButton.click()
			time.sleep(7)


			browser.get('https://meet.google.com')
			time.sleep(7)


			if(browser.find_elements_by_xpath('//*[@id="authzenNext"]/div/button/div[2]')):
				context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
				context.bot.send_message(chat_id=update.message.chat_id, text="Need Verification. Please Verify")
				browser.find_element_by_xpath('//*[@id="authzenNext"]/div/button/div[2]').click()
				time.sleep(5)

				browser.save_screenshot("ss.png")
				context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
				mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
				os.remove('ss.png')
				time.sleep(20)

			pickle.dump( browser.get_cookies() , open("meet.pkl","wb"))
			context.bot.send_message(chat_id=update.message.chat_id, text="Logged In!")
		
		browser.get(url_meet)
		time.sleep(3)

		browser.save_screenshot("ss.png")
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
		mid  = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), caption="joining", timeout = 120).message_id
		os.remove('ss.png')
		try:
			ActionChains(browser).key_down(Keys.CONTROL).send_keys('e').key_up(Keys.CONTROL).perform()
			time.sleep(2)
			try:
				ActionChains(browser).key_down(Keys.CONTROL).send_keys('d').key_up(Keys.CONTROL).perform()
				time.sleep(2)
			except:
				context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
				context.bot.send_message(chat_id=update.message.chat_id, text="Cannot off your microphone")
		except:
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
			context.bot.send_message(chat_id=update.message.chat_id, text="cannot off your video")
			

		if(browser.find_elements_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div')):
			browser.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div').click()
			time.sleep(3)

			context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)

			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')
		try:
			browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]").click()
			time.sleep(10)
		except:
			browser.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Join now')]").click()
			time.sleep(10)

		context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)
		time.sleep(5)
		browser.save_screenshot("ss.png")
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
		mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
		os.remove('ss.png')

		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		context.bot.send_message(chat_id=update.message.chat_id, text="Attending you lecture. You can chill")
		global logged_in
		logged_in=True
		context.bot.send_message(chat_id=update.message.chat_id,text="To exit click /exitmeet ")
		context.bot.send_message(chat_id=update.message.chat_id,text="Please send /status to check status😉")
		pause
		logging.info("joined Gmeet")
		time.sleep(3)
		context.bot.delete_message(chat_id=update.message.chat_id,message_id=mid)

		
	except:
		browser.execute_script("window.open('');")
		browser.close()
		browser.switch_to.window(browser.window_handles[-1])
		context.bot.send_message(chat_id=update.message.chat_id, text="Some error occurred retry!")
		logging.info("Cannot attend Gmeet")

def exitmeet(update,context):
	global logged_in
	if logged_in:
		try:
			logging.info("exiting meet!!!")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
			context.bot.send_message(chat_id=update.message.chat_id, text="Exiting your meeting!!")
			browser.execute_script("window.open('');")
			browser.close()
			browser.switch_to.window(browser.window_handles[-1])
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
			context.bot.send_message(chat_id=update.message.chat_id, text="Exited your meeting.")
			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')
			time.sleep(10)
			context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)
			
		except:
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
			context.bot.send_message(chat_id=update.message.chat_id, text="Some error occured!!!retry again.")
	else:
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		context.bot.send_message(chat_id=update.message.chat_id, text="No meeting is running to exit.")
def gchat(update,context):
	msg=update.message.text.split()[-1]
	if msg != '/gchat':
		global logged_in
		if logged_in:
			try:
				ActionChains(browser).key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('c').key_up(Keys.ALT).key_up(Keys.CONTROL).perform()
				time.sleep(2)
				ActionChains(browser).send_keys(msg).perform()
				time.sleep(2)
				ActionChains(browser).send_keys(Keys.ENTER).perform()
				time.sleep(2)
				browser.save_screenshot("ss.png")
				context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
				mid1 = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'),caption='message sent:'+str(msg), timeout = 120).message_id
				os.remove('ss.png')
				ActionChains(browser).send_keys(Keys.ESCAPE).perform()
				time.sleep(2)
				browser.save_screenshot("ss.png")
				context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
				mid2 = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
				os.remove('ss.png')
				time.sleep(10)
				context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid1)
				context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid2)
			except:
				context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
				context.bot.send_message(chat_id=update.message.chat_id, text="cannot send message.")

		else:
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
			context.bot.send_message(chat_id=update.message.chat_id, text="No meeting is running to send message.")
	else:
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		context.bot.send_message(chat_id=update.message.chat_id, text="please send a valid message")


def start(update,context):
	context.bot.send_message(chat_id=update.message.chat_id,text="Use following Commands to interact with bot :\nTo join google meet - /meet Gmeetlink\n To Send messages in Gmeet - /gchat yourmessage \nTo join zoom meeting - /zoom zoommeetingid password\nTo know Status of Bot - /status\nTo exit Gmeet - /exitmeet\nTo restart Bot🤖 - /restart")
	
def loginteams(update,context):
	logging.info("logging in teams account")
	try:
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		usernameStr = Config.TEAMSUSERNAME
		passwordStr = Config.TEAMSPASSWORD
		# url_meet = update.message.text.split()[-1]


		browser.get('https://teams.microsoft.com')
		# time.sleep(2)
		context.bot.send_message(chat_id=update.message.chat_id, text="logging in")
		try:
			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')
			emailField = browser.find_element_by_xpath('//*[@id="i0116"]')
			emailField.click()
			emailField.send_keys(usernameStr)
			browser.find_element_by_xpath('//*[@id="idSIButton9"]').click() #Next button
			time.sleep(5)
			context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)
		except:
			context.bot.send_message(chat_id=update.message.chat_id, text="unable to enter email")
			context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)
		try:
			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')
			passwordField = browser.find_element_by_xpath('//*[@id="i0118"]')
			passwordField.click()
			passwordField.send_keys(passwordStr)
			browser.find_element_by_xpath('//*[@id="idSIButton9"]').click() #Sign in button
			time.sleep(5)
			context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)
		except:
			context.bot.send_message(chat_id=update.message.chat_id, text="unable to enter password")
			context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)
		pickle.dump( browser.get_cookies() , open("teams.pkl","wb"))
		context.bot.send_message(chat_id=update.message.chat_id, text="Logged In!...please click JOINTEAMS 'class_name' to join class...")
		global teams_in
		teams_in=True
	except:
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		context.bot.send_message(chat_id=update.message.chat_id, text="Some error occured!!!retry again.")
def jointeams(update,context):
	global teams_in
	if teams_in:
		class_name=update.message.text.split()[-1]
		browser.get('https://teams.microsoft.com/')
		time.sleep(5)
		try:
			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')
			
			classes_available = browser.find_elements_by_class_name("name-channel-type")
			for i in classes_available:
				if class_name.lower() in i.get_attribute('innerHTML').lower():
					print("JOINING CLASS ",class_name)
					i.click()
					break
			context.bot.send_message(chat_id=update.message.chat_id, text="joining class"+str(class_name))
			time.sleep(4)
			context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)
			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')
			try:
				joinbtn = browser.find_element_by_class_name("ts-calling-join-button")
				joinbtn.click()

			except:
				#join button not found
				#refresh every minute until found
				k = 1
				while(k<=5):
					context.bot.send_message(chat_id=update.message.chat_id, text="joining button not found trying again!! wating for "+str(5-k)+" more minutes")
					time.sleep(55)
					browser.refresh()
					time.sleep(5)
					try:
						joinbtn = browser.find_element_by_class_name("ts-calling-join-button")
						joinbtn.click()
						break
					except:
						pass
					# schedule.every(1).minutes.do(joinclass,class_name,start_time,end_time)
					k+=1
				context.bot.send_message(chat_id=update.message.chat_id, text="seems like there is no class today!!")
			time.sleep(4)
			context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)
			webcam = browser.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
			if(webcam.get_attribute('title')=='Turn camera off'):
				webcam.click()
				context.bot.send_message(chat_id=update.message.chat_id, text="camera turned off")
			time.sleep(3)

			microphone = browser.find_element_by_xpath('//*[@id="preJoinAudioButton"]/div/button/span[1]')
			if(microphone.get_attribute('title')=='Mute microphone'):
				microphone.click()
				context.bot.send_message(chat_id=update.message.chat_id, text="microphone turned off")
			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')
			time.sleep(3)

			context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)
			joinnowbtn = browser.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
			joinnowbtn.click()

			context.bot.send_message(chat_id=update.message.chat_id, text="successfully joined......")
			context.bot.send_message(chat_id=update.message.chat_id, text="please click /exitteams to exit class")
			time.sleep(2)
			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')
			time.sleep(3)
			context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)
		except:
			context.bot.send_message(chat_id=update.message.chat_id, text="some error occurred please /restart......")
	else:
		context.bot.send_message(chat_id=update.message.chat_id, text="/loginteams first to attend class")
def exitteams(update,context):
	global teams_in
	if teams_in:
		try:
			browser.find_element_by_class_name("ts-calling-screen").click()
			browser.find_element_by_xpath('//*[@id="teams-app-bar"]/ul/li[3]').click() #come back to homepage
			time.sleep(3)
			browser.find_element_by_xpath('//*[@id="hangup-button"]').click()
			context.bot.send_message(chat_id=update.message.chat_id, text="exited your class..")
			browser.execute_script("window.open('');")
			browser.close()
			browser.switch_to.window(browser.window_handles[-1])
			browser.save_screenshot("ss.png")
			context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
			mid = context.bot.send_photo(chat_id=update.message.chat_id, photo=open('ss.png', 'rb'), timeout = 120).message_id
			os.remove('ss.png')
			time.sleep(3)
			context.bot.delete_message(chat_id=update.message.chat_id ,message_id = mid)
		except:
				context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
				context.bot.send_message(chat_id=update.message.chat_id, text="Some error occured!!!retry again.")
	else:
		context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
		context.bot.send_message(chat_id=update.message.chat_id, text="Some error occured!!!retry again.")

def main():
	import os
	# PORT = int(os.environ.get('PORT', 8000))
	dp.add_handler(CommandHandler("start",start))
	dp.add_handler(CommandHandler("zoom", zoom))
	dp.add_handler(CommandHandler("meet", meet))
	dp.add_handler(CommandHandler("restart", restart))
	dp.add_handler(CommandHandler("status", status))
	dp.add_handler(CommandHandler("exitmeet", exitmeet))
	dp.add_handler(CommandHandler("gchat", gchat))
	dp.add_handler(CommandHandler("loginteams", loginteams))
	dp.add_handler(CommandHandler("jointeams", jointeams))
	dp.add_handler(CommandHandler("exitteams", exitteams))
	logging.info("Bot started")
	# updater.start_webhook(listen="0.0.0.0",
 #                          port=int(PORT),
 #                          url_path=str(Config.BOT_TOKEN))
	# updater.bot.setWebhook('https://charanclassesbot.herokuapp.com/' + str(Config.BOT_TOKEN))
	updater.start_polling()

if __name__ == '__main__':
    main()