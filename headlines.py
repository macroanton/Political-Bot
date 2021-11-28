import praw
import random
import datetime
import time
import pprint
from praw.models import InlineGif, InlineImage, InlineVideo

reddit = praw.Reddit('bot')

submission_url= 'https://www.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission = reddit.submission(url=submission_url)
while True:
    for posts in reddit.subreddit("news").hot(limit=200):
        # print(submission.url)
        # print(submission.author)
    # pprint.pprint(vars(posts))
        print()
        print('new iteration at:',datetime.datetime.now())
        print('submission.title=',posts.title)
        print('submission.url=',posts.url)
        url= posts.url
        title= posts.title
        image = InlineImage(posts.thumbnail)
        reddit.subreddit("BotTown2").submit(title, url=url) #inlinemedia=image)
        time.sleep(15)
