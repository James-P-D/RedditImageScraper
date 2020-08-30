import praw # https://praw.readthedocs.io/en/latest/
import argparse
from os import sys, path, mkdir
from urllib.parse import urlparse
import requests
import configparser

###############################################
# download_images()
###############################################

def download_images(sub_reddits, sub_reddit_download_total, overall_total, download_folder):
    config = configparser.ConfigParser()
    config.read("config.ini")

    reddit = praw.Reddit(client_id=config['REDDIT']['client_id'],         # From https://www.reddit.com/prefs/apps/
                         client_secret=config['REDDIT']['client_secret'], # From https://www.reddit.com/prefs/apps
                         user_agent="testscript by /u/jddddddddddd")

    if not path.exists(download_folder):
        mkdir(download_folder)

    downloaded = 0
    for sub_reddit in sub_reddits:
        sub_reddit_downloaded = 0
        print("Downloading from", sub_reddit)
        for submission in reddit.subreddit(sub_reddit).hot(limit=sub_reddit_download_total):
            if(submission.url.endswith(("jpg", "jpeg", "png"))):
                filename = path.basename(urlparse(submission.url).path)
                downloader = requests.get(submission.url, allow_redirects=True)
                open(download_folder + "\\" + filename, 'wb').write(downloader.content)
                print(filename)
                downloaded += 1
                sub_reddit_downloaded += 1
                if (downloaded >= overall_total):
                    break
        print("Downloaded", sub_reddit_downloaded, "from", sub_reddit)
        print()
    print("Downloaded", downloaded, "from", len(sub_reddits), "sub-reddits")

###############################################
# main()
###############################################

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
                        default=1000,
                        type=int,
                        help="total images per subreddit to download")
    parser.add_argument('-t',
                        metavar="total",
                        type=int,
                        default=100000,
                        help="total images overall to download")
    parser.add_argument('-f',
                        metavar="folder",
                        type=str,
                        default="download",
                        help="folder to save images to")

    args = parser.parse_args()
    download_images(args.r, args.st, args.t, args.f)

###############################################
# Startup
###############################################

if __name__ == "__main__":
    main()
