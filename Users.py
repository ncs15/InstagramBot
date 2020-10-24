import datetime, TimeHandler
import ConfigHandler
import sqlite3
import random

db_name = "dbo.db"


#delete user by username
def delete_user(username):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    sql = "DELETE FROM followed_users WHERE username = '{0}'".format(username)
    cursor.execute(sql)
    conn.commit()


#add new username
def add_user(username):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO followed_users(username, date_added) VALUES(?  ,?)",(username, now))
    conn.commit()

#in progress
def add_viewed_user(username,followers_list):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO viewed_users(username,followers_list,followers_no,following_no,another_info,viewed_date) VALUES(? ,?,?,?,?,?)",(username,followers_list,"na","na","na", now))
    conn.commit()

#in progress
def add_legacy_user(username):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO legacy_users(username, date_inserted) VALUES(?, ?)",(username, now))
    conn.commit()
    
def add_liked_user(username):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO liked_users(username, date_firts_like, photo1_id) VALUES(?, ?, ?)",(username, now, "tbd"))
    conn.commit()

#check if any user qualifies to be unfollowed
def check_unfollow_list():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM followed_users")
    results = cursor.fetchall()
    users_to_unfollow = []
    for r in results:
        d = TimeHandler.days_since_date(r[1])
        if d >= ConfigHandler.DAYS_TO_UNFOLLOW:
            users_to_unfollow.append(r[0])
    return users_to_unfollow


#get all followed users
def get_followed_users():
    users = []
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM followed_users")
    results = cursor.fetchall()
    for r in results:
        users.append(r[0])

    return users

#get the numer of people that you follow in that day
def get_today_followed():
  conn = sqlite3.connect(db_name)
  cursor = conn.cursor()
  now = datetime.datetime.now().date()
  try:
    cursor.execute(f"SELECT * FROM followed_users WHERE date_added='{now}'")
    results = cursor.fetchall()
  except:
    results=[]

  no=0
  for r in results:
    no+=1
  return no


def get_viwed_users(all=True):
  users = []
  conn = sqlite3.connect(db_name)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM viewed_users")
  results = cursor.fetchall()
  res=0
  if all==True:
      for r in results:
          users.append(r[0])
      response=users
  else:
      for r in results:
        res+=1
        users.append([r[0],r[1]])
      response=users[random.randint(0, res-1)]
  return response;


def update_viwed(user_to_keep, interest_user):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    user = interest_user[0]
    now = datetime.datetime.now().date()
    sql = "DELETE FROM viewed_users WHERE username = '{0}'".format(user)
    cursor.execute(sql)
    cursor.execute("INSERT INTO viewed_users(username,followers_list,followers_no,following_no,another_info,viewed_date) VALUES(? ,?,?,?,?,?)",(user,user_to_keep,"na","na","na", now))
    print("Update viwed seq done!")
    conn.commit()