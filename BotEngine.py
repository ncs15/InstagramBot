import AgentLogic, DBUsers
import ConfigHandler
import time
import datetime
from AgentLogic import IGBot
import random

def init(webdriver):
    ConfigHandler.init()
    bot = IGBot()
    try:
        bot.login(webdriver)
    except:
        print("Login Error")
    time.sleep(2)



def update(webdriver):
    bot = IGBot()
    while True:
        event=random.randint(1,4)
        print("Event: ",event)
        if event == 1:
            bot.like_on_home(webdriver)
        elif event == 2:
            check_followers(webdriver)
        elif event == 3:
            bot.check_hashtag(webdriver)
        elif event == 4:
            bot.interest_circle(webdriver)
        else:
            print(datetime.datetime.now(), ' Sleep for 100-250 sec')
            time.sleep(random.randint(90, 150))

        print(datetime.datetime.now(), ' Sleep for 200-350 sec')
        time.sleep(random.randint(200, 350))


def check_followers(webdriver):
    bot = IGBot()
    print("Checking for users to unfollow...")
    #get the unfollow list
    users = DBUsers.check_unfollow_list()
    #if there's anyone in the list, start unfollowing operation
    if len(users) > 0:
        print(f"You follow some people for more than {ConfigHandler.DAYS_TO_UNFOLLOW} days")
        bot.unfollow_people(webdriver, users)