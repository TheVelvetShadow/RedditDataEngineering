import praw
from praw import Reddit
import sys

def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent)
        print("Connected to Reddit.")
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1) 

def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)

    #post_lists = []

    print(posts)


    # for post in posts:
    #     post_dict = vars(post)
    #     post = {key: post_dict[key] for key in POST_FIELDS}
    #     post_lists.append(post)

    # return post_lists        
