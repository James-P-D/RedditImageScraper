import argparse

#https://www.reddit.com/r/redditdev/comments/ah4itf/python_webscraping_images_from_reddit/
#https://praw.readthedocs.io/en/latest/

def main():
    parser = argparse.ArgumentParser(description="Download images from reddit")
    parser.add_argument("sub_reddits",
                        metavar="sub_reddits",
                        type=str,
                        nargs="+",
                        help="list of subreddits")
    parser.add_argument('--total_subreddit',
                        metavar="total_subreddit",
                        default=100,
                        type=int,
                        help="total images per subreddit to download")
    parser.add_argument('--total',
                        metavar="total",
                        type=int,
                        default=1000,
                        help="total images overall to download")
    parser.add_argument('--folder',
                        metavar="folder",
                        type=str,
                        default="download",
                        help="folder to save images to")

    args = parser.parse_args()
    
    print(args.sub_reddits)
    print(args.total_subreddit)
    print(args.total)
    print(args.folder)
    print("foo")

###############################################
# Startup
###############################################

if __name__ == "__main__":
    main()
