from time import sleep
import datetime
import DBUsers, ConfigHandler
import traceback
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class IGBot:
    def __init__(self):
        self.loginpage_link='https://www.instagram.com/accounts/login/?source=auth_switcher'
        self.home_page_link='https://www.instagram.com/'
        self.unfollow_xpath = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button'
        self.follow_button_xpath='//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button'

                                #'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button'
        self.unfollow_confirm_xpath = '/html/body/div[4]/div/div/div/div[3]/button[1]'
        self.article_four='//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[4]'
        self.article_four_like_button= '//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[4]/div[3]/section[1]/span[1]/button'
        self.article_five='//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[5]'
        self.article_five_like_button='//*[@id="react-root"]/section/main/section/div[1]/div[2]/div/article[5]/div[3]/section[1]/span[1]/button'
        self.first_post_hastag='//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]'
        self.username_hashtag_selector='body > div._2dDPU.CkGkG > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > span > a'
        self.no_likes_xpath='/html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div/button/span'
        self.no_likes_xpath_second='/html/body/div[3]/div[2]/div/article/div[3]/section[2]/div/div/button/span'
        self.hashtag_follow_xpath='/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button'
        self.hashtag_like_button='/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div'
        self.button_next_secondpost='/html/body/div[4]/div[1]/div/div/a[2]'
        self.button_next_firstpost='/html/body/div[4]/div[1]/div/div/a'
        self.cookie_button ='/html/body/div[2]/div/div/div/div[2]/button[1]'

    def login(self,webdriver):

        #Open the instagram login page
        print(datetime.datetime.now(),"@@@@@@@@@  Login")
        webdriver.get(self.loginpage_link)
        #sleep for 3 seconds to prevent issues with the server
        sleep(3)
        webdriver.find_element_by_xpath(self.cookie_button).click()
        sleep(1)
        #Find username and password fields and set their input using our constants
        username = webdriver.find_element_by_name('username')
        username.send_keys(ConfigHandler.INST_USER)
        password = webdriver.find_element_by_name('password')
        password.send_keys(ConfigHandler.INST_PASS)
        sleep(1)
        #Get the login button
        try:
            button_login = webdriver.find_element_by_xpath(
                '//*[@id="loginForm"]/div/div[3]/button')
        except:
            print("Login Error!")
        #sleep again
        sleep(4)
        #click login
        button_login.click()
        sleep(4)
        #In case you get a popup after logging in, press not now.
        #If not, then just return
        try:
            notnow = webdriver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div/div/section/div/button')
            print("Not now popup detected")
            notnow.click()
            print("Pop up closed")
        except:
            print("No pop up")
        sleep(4)
        try:
            notify = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            print("Notification popup detected")
            notify.click()
            print("Pop up closed")
        except:
            print("No pop up")


    def unfollow_people(self,webdriver, people):
        print("_______________________________________Start Unfollow sequence_________________________________________________________________")
        flag_max_unfollow=0
    
        for user in people:
            #Set a max iteration in a run for no of unfollow
            flag_max_unfollow+=1
            if flag_max_unfollow<random.randint(15, 20):
                try:
                    webdriver.get('https://www.instagram.com/' + user + '/')
                    print("Got to: ", user)
                    sleep(random.randint(4, 8))
                    unfollow_button = webdriver.find_element_by_xpath(self.unfollow_xpath)
                    unfollow_txt = unfollow_button.find_element_by_css_selector("span").get_attribute("aria-label")
                    if unfollow_txt == "Following":
                       sleep(random.randint(4, 8))
                       webdriver.find_element_by_xpath(self.unfollow_xpath).click()
                       sleep(random.randint(2, 3))
                       webdriver.find_element_by_xpath(self.unfollow_confirm_xpath).click()
                       print(datetime.datetime.now()," Unfollowing:",user)
                       sleep(random.randint(3, 5))
                       DBUsers.delete_user(user)
    
                except Exception:
                    #is is possible that i already unfollow that user manually, so just delte it from db
                    print(datetime.datetime.now()," Ecxept unfollow: ",user)
                    DBUsers.delete_user(user)
                    traceback.print_exc()
                    continue
            else:
                continue
        print(
            "_______________________________________Stop Unfollow sequence_________________________________________________________________")

        
    def like_on_home(self,webdriver):
    
        print("_________________________________________________Start Like on home____________________________________________________")
        print(datetime.datetime.now())
        webdriver.get(self.home_page_link) #goto homepage
        sleep(random.randint(1, 2))
        body = webdriver.find_element_by_tag_name('body') #scroll in order to load the page
        body.send_keys(Keys.DOWN)
        body.send_keys(Keys.DOWN)
        body.send_keys(Keys.DOWN)
        sleep(random.randint(8, 12))
        try:
            article = webdriver.find_element_by_xpath(self.article_four) #find article 4 and like it in order to load next articles
        except:
            body.send_keys(Keys.DOWN)
            body.send_keys(Keys.DOWN)
            body.send_keys(Keys.DOWN)

        button = article.find_element_by_xpath(self.article_four_like_button)
        button.click()
        sleep(3)
        #start looping through posts
        for i in range(1,random.randint(15, 19)):
    
            for i in range(0,random.randint(1, 2)):
                body.send_keys(Keys.DOWN) #scroll in order to load the page
    
            article = webdriver.find_element_by_xpath(self.article_five) #delete?
            sleep(random.randint(2, 5))
            if random.randint(0, 100) < ConfigHandler.LIKE_RATIO:
                like_if = True
            else:
                like_if = False

            try:
                #try to find if the post is already liked
                like_button = webdriver.find_element_by_xpath(self.article_five_like_button)
                like_txt = like_button.find_element_by_css_selector("svg").get_attribute("aria-label")
            except:
                like_txt = "no"

            sleep(random.randint(2, 3))

            if like_if == True and like_txt == "Like":   #like the post if like is different from 1 --> how many like to give
                button_like = webdriver.find_element_by_xpath(self.article_five_like_button)
                sleep(random.randint(2, 3))
                button_like.click()
                print("Like")
            else:
                #if the page is not properly loaded then go to next post in oredr to reload the page elements
                actions=ActionChains(webdriver)
                actions.move_to_element(like_button).perform()
        print("______________________________________________Stop Like on home_________________________________________________________")


    def check_hashtag(self,webdriver):
        print(datetime.datetime.now(),
              "_______________________________ Follow people sequence on______________________________________________")

        # Iterate random theough all the hashtags from the constants
        hastag_list = list(ConfigHandler.HASHTAGS)
        for hashtag in random.sample(hastag_list, len(hastag_list)):
            print(datetime.datetime.now(), f" Goto '{hashtag}' hastag")
            # Visit the hashtag
            try:
                webdriver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
                sleep(random.randint(5, 10))
            except:
                print("Can't go to hastag: ",hashtag)
                break
            # Get the first post thumbnail and click on it
    
            first_post = webdriver.find_element_by_xpath(self.first_post_hastag)
            first_post.click()
            print("Open first post")
    
            sleep(random.randint(3, 10))
    
            try:
                # iterate over the first random posts in the hashtag
    
                random_pick = random.randint(25, 35)
                for x in range(1, random_pick):
                    print(
                        "_______________________________________________________________________________________________________")
                    t_start = datetime.datetime.now()
                    # Get the poster's username
                    username = webdriver.find_element_by_css_selector(self.username_hashtag_selector).text
    
                    print(datetime.datetime.now(), "Interaction with :", username)

                    sleep(random.randint(3, 11))
                    
                    likes_over_limit = False
                    try:
                        # get number of likes and compare it to the maximum number of likes to ignore post
                        try:
                            likes = int(webdriver.find_element_by_xpath(self.no_likes_xpath).text.replace(",",""))

                        except:
                            try:
                                likes = int(webdriver.find_element_by_xpath(self.no_likes_xpath_second).text.replace(",", ""))
                            except:
                                print("Can't find no of likes, check for a second xpath! Default=1")
                                likes = 1

                        print("NO of likes:", likes)

                        likes_over_limit = False
                        if likes > ConfigHandler.LIKES_LIMIT:
                            likes_over_limit = True
                        
                        # If username isn't stored in the database and the likes are in the acceptable range, follow change =25%

                        followed_users = DBUsers.get_today_followed()


                        if random.randint(0, 100) < ConfigHandler.FOLLOW_RATIO:
                            follow_if = True
                        else:
                            follow_if = False

                        if not likes_over_limit and follow_if == True and followed_users < ConfigHandler.MAX_FOLLOWED_PER_DAY:
                            #   #Don't press the button if the text doesn't say follow
                            print("Today you followed: ", followed_users, " new users")
                            sleep(random.randint(3, 11))
                            
                            try:

                                if webdriver.find_element_by_xpath(self.hashtag_follow_xpath).text == 'Follow':
    
                                    # Click follow
                                    sleep(3)
                                    webdriver.find_element_by_xpath(self.hashtag_follow_xpath).click()
    
                                    print("Followed: {0}, #{1}".format(username, followed_users))
    
                                    try:
                                        DBUsers.add_user(username)
                                        print(datetime.datetime.now(), " Add to db: ", username)
                                    except:
                                        print("User already in db")
                            except:
                                print("Follow label finding error!!")
                                break
                            # Liking the picture

                        sleep(2)

                        if random.randint(0, 100) < ConfigHandler.LIKE_RATIO:
                            like_if=True
                        else:
                            like_if= False

                        print("Give Like: ", like_if)
                        try:
                            like_button = webdriver.find_element_by_xpath(self.hashtag_like_button)
                            like_txt = like_button.find_element_by_css_selector("svg").get_attribute("aria-label")
                        except:
                            print("No like text found!")

                        if like_if == True and like_txt == "Like":
                            try:
                                button_like = webdriver.find_element_by_xpath(self.hashtag_like_button)

                                if button_like:
                                    sleep(3)
                                    button_like.click()
                                    print(datetime.datetime.now(), " Like photo of: ", username)
                                else:
                                    button_like = webdriver.find_element_by_xpath(self.hashtag_like_button)
                                    sleep(3)
                                    button_like.click()
                                    print(datetime.datetime.now(), " Like photo of: ", username)
                                    # Use DBUsers to add the new user to the database
                                try:
                                    DBUsers.add_liked_user(username)
                                    print("DB: Add to liked users: ", username)
                                except:
                                    print("DB: user already liked")
                            except:
                                print("Can't find like button.If persist, check xpath!")
                                break
    
                        # Next picture
    
                        sleep(random.randint(2, 9))
                        try:
                            button_next = webdriver.find_element_by_xpath(self.button_next_secondpost)
                            button_next.click()
                        except:
                            try:
                                button_next = webdriver.find_element_by_xpath(self.button_next_firstpost)
                                button_next.click()
                            except:
                                body = webdriver.find_element_by_tag_name('body')
                                body.send_keys(Keys.RIGHT)
    
                        sleep(random.randint(2, 7))
    
                    except:
                        traceback.print_exc()
                        continue
            except:
                traceback.print_exc()
                continue
    
                pass
            webdriver.get(self.home_page_link)
            print(datetime.datetime.now(),
                  "_______________________________ Follow people sequence off______________________________________________")



    def getUserFollowers(self,webdriver,int_user):
        max = 200
        webdriver.get('https://www.instagram.com/' + int_user)
        sleep(2)
        followersLink = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')

        followersLink.click()
        sleep(2)
        followersList = webdriver.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

        followersList.click()
        actionChain = ActionChains(webdriver)
        body = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        actionChain.double_click(body).perform()
        endtime = time.time() + 10.0

        while True:
            actionChain.key_down(Keys.SPACE).perform()

            if time.time() > endtime:
                actionChain.key_up(Keys.SPACE).perform()
                break

        actionChain.double_click(body).perform()
        endtime = time.time() + 10.0
        while True:
            actionChain.key_down(Keys.SPACE).perform()

            if time.time() > endtime:
                actionChain.key_up(Keys.SPACE).perform()
                break

        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

        print(numberOfFollowersInList)

        followers = []
        try:
            for user in followersList.find_elements_by_css_selector('li'):
                userLink = user.find_element_by_css_selector('a').get_attribute("href")
                userLink = userLink[26:-1]
                # print(userLink)
                followers.append(userLink)

                if (len(followers) == max):
                    break
        except:
            pass
        DBUsers.add_viewed_user(str(int_user), str(followers))


        return followers

    def follow_user(self, webdriver, user):
        webdriver.get('https://www.instagram.com/' + user + '/')
        print("Got to: ", user)
        sleep(random.randint(4, 8))
        try:
            follow_button = webdriver.find_element_by_xpath(self.follow_button_xpath)
            follow_button.click()
            DBUsers.add_user(user)
        except:
            print("Account is private/already followed in the pas or following")
        print(datetime.datetime.now(), " Following:", user)
        sleep(random.randint(2, 3))


    def interest_circle(self, webdriver):
        print(ConfigHandler.INT_USERS)
        for user in list(ConfigHandler.INT_USERS):
            if user in DBUsers.get_viwed_users(all=True):
                print(user)
            else:
                IGBot().getUserFollowers(webdriver,user)
        interest_users=DBUsers.get_viwed_users(all=False)
        print(len(interest_users))
        if len(interest_users) >= 2:
            interest_users[1] = interest_users[1][1:-1]
            for_follow = interest_users[1].replace("'", "").split(",")[:7]
            for_modify = interest_users[1].replace("'", "").split(",")[8:]
            user_to_keep = []
            for i in for_modify:
                i = i.replace(" ","")
                user_to_keep.append(i)
            user_to_keep = str(user_to_keep)
            DBUsers.update_viwed(user_to_keep, interest_users)
            print(user_to_keep)
            print(for_follow)
            for user in for_follow:
                IGBot().follow_user(webdriver ,user.strip())


        else:
            pass

