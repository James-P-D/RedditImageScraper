import praw # https://praw.readthedocs.io/en/latest/
import argparse
from os import sys, path
from urllib.parse import urlparse
import requests
import configparser

def main():
    parser = argparse.ArgumentParser(description="Download images from reddit")
    parser.add_argument("-r",
                        metavar="sub_reddits",
                        type=str,
                        nargs="+",
                        required="true",
                        help="list of subreddits")
    parser.add_argument('-st',
                        metavar="total_subreddit",
                        default=100,
                        type=int,
                        help="total images per subreddit to download")
    parser.add_argument('-t',
                        metavar="total",
                        type=int,
                        default=1000,
                        help="total images overall to download")
    parser.add_argument('-f',
                        metavar="folder",
                        type=str,
                        default="download",
                        help="folder to save images to")

    args = parser.parse_args()
    
    print("sub_reddits = ", args.r)
    print("total_subreddit = ", args.st)
    print("total = ", args.t)
    print("folder = ", args.f)


    config = configparser.ConfigParser()
    config.read("config.ini")

    reddit = praw.Reddit(client_id=config['REDDIT']['client_id'],         # From https://www.reddit.com/prefs/apps/
                         client_secret=config['REDDIT']['client_secret'], # From https://www.reddit.com/prefs/apps
                         user_agent="testscript by /u/jddddddddddd")

    #for submission in reddit.subreddit("dogpictures").hot(limit=None):
    for submission in reddit.subreddit("dogpictures").hot(limit=10):
        if(submission.url.endswith(("jpg", "jpeg", "png"))):
            a = urlparse(submission.url)
            b = path.basename(a.path)
            r = requests.get(submission.url, allow_redirects=True)
            open(b, 'wb').write(r.content)
            print(b)
            
    
    print("Done!")
###############################################
# Startup
###############################################

if __name__ == "__main__":
    main()
