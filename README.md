# IstagramBot

This is a easy to use bot for an organic growing of IG account.

# What the bot can do?

Well... the bot can:
-loop through predefine by user hashtags, like the post and follow the user which posted it at a predefined rate;
-unfollow people after a predefine number of days;
-scroll on newsfeed and like those posts in order to engage allready following people to like your posts;
-search for those people that are following an account that interests you and follow them ( if you are a fan of cars, the bot will connect you with cars fans).
-run in the backgrond...so no distraction for you.


Instruction.

1. Modify "executable_path" from Main.py with your path to chromdriver;
2. Modify the settings.py:

	-user and pass from IG account;
	
	-headless --> yes/no (yes if you want to run the bot in the background);
	
	-like and follow ratio, (75% and 25% are the defaults).. this is in order to avoid any IG problems:D;
	
	-days_to_unfollow --> the number of days to keep the followed users;
	
	-max_followed_per_day --> the top limit of followed users per day;
	
	-likes_over --> over this top, the bot do not give likes;
	
	-int_users --> the users of interest in order to gain followers from an area;
	
	-hashtags --> the hastags where the bot find new users.
	
3. Run Main.py

