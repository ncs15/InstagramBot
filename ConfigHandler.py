import json
INST_USER= INST_PASS= USER= PASS= HOST= DATABASE= POST_COMMENTS = ''
LIKES_LIMIT=DAYS_TO_UNFOLLOW=0
HASHTAGS = []
HEADLESS=""
DATABASE=""
MAX_FOLLOWED_PER_DAY=0
INT_USERS=""
LIKE_RATIO=0
FOLLOW_RATIO=0

def init():
    global INST_USER, INST_PASS, USER, PASS, HOST, DATABASE,\
        LIKES_LIMIT, DAYS_TO_UNFOLLOW, HASHTAGS, MAX_FOLLOWED_PER_DAY, DATABASE, HEADLESS,INT_USERS,LIKE_RATIO,FOLLOW_RATIO
    # read file
    data = None
    with open('settings.json', 'r', encoding="cp437", errors='ignore') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    INST_USER = obj['instagram']['user']
    INST_PASS = obj['instagram']['pass']
    DATABASE = obj['db']['database']
    LIKES_LIMIT = obj['config']['likes_over']
    HASHTAGS = obj['config']['hashtags']
    DAYS_TO_UNFOLLOW = obj['config']['days_to_unfollow']
    MAX_FOLLOWED_PER_DAY = obj['config']['max_followed_per_day']
    HEADLESS = obj['config']['headless']
    INT_USERS = obj['config']['int_users']
    LIKE_RATIO = obj['config']['like_ratio']
    FOLLOW_RATIO = obj['config']['follow_ratio']

