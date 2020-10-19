# IstagramBot

This is a easy to use bot for an organic growing of IG account.

# What the bot can do?

Well... the bot can:

-Sing in;

-Loop through hashtags posts, like it and follow the posters at a predefine rate;

-Like posts from your feed;

-Unfollow users after a preset number of days;

-Building an audience in a certain sector by providing as an input a list of a few well known users and interact with the followers of those users (if you like cars, you set the 
usernames of a few pages that posts cars and the bot will do the rest);

-Running the bot in the background if you want a cleaner approach;

-All should be as random as it can be in order to mimic human behavior.


# Instruction.

1. Modify "executable_path" from Main.py with your path to chromdriver;
2. Modify the settings.py:


-headless → yes/no (yes if you want to run the bot in the background);

-like and follow ratio, (75% and 25% are the defaults)… this is in order to avoid any IG problems. Basically you like 75 posts from 100.

-days_to_unfollow → the number of days to keep following the users;

-max_followed_per_day → the top limit of followed users per day;

-likes_over → if a post has more than this limit, the bot would not give any like to that particulary post;

-int_users → the users of interest in order to gain followers from an area;

-hashtags → the hastags where the bot finds new users.
	
3. Run Main.py



See more info on the following medium post:

https://python-noob.medium.com/instagram-bot-with-selenium-for-learning-web-testing-tools-fbe424c9ebe9
