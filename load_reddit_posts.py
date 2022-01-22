import argparse # pragma: no cover 
from datetime import datetime # pragma: no cover
from random import randint # pragma: no cover

import praw # pragma: no cover

from app import app, config, db # pragma: no cover
from app.models import Category, Post, User # pragma: no cover

parser = argparse.ArgumentParser(description='Load posts from a subreddit.') # pragma: no cover
parser.add_argument('subreddit', metavar='subreddit', nargs='?', default='learnpython', # pragma: no cover
                    help='the subreddit to load (default is learnpython') # pragma: no cover
args = parser.parse_args() # pragma: no cover
subreddit = args.subreddit # pragma: no cover

app.config.from_object(config.Config) # pragma: no cover
app.config.from_envvar('WOLFIT_SETTINGS') # pragma: no cover


def create_user(subreddit): # pragma: no cover
    username = f"{subreddit}-{randint(0, 999999)}" # pragma: no cover
    u = User(username=username, email=f"{username}@example.com") # pragma: no cover
    u.set_password('wolfit') # pragma: no cover
    db.session.add(u) # pragma: no cover
    db.session.commit() # pragma: no cover
    return u # pragma: no cover


def create_category(subreddit): # pragma: no cover
    category = None # pragma: no cover
    category = Category.query.filter_by(title=subreddit).first() # pragma: no cover
    if category is None: # pragma: no cover
        category = Category(title=subreddit) # pragma: no cover
        db.session.add(category) # pragma: no cover
        db.session.commit() # pragma: no cover
    return category # pragma: no cover


reddit = praw.Reddit() # pragma: no cover

u = create_user(subreddit) # pragma: no cover
c = create_category(subreddit) # pragma: no cover

for submission in reddit.subreddit(subreddit).hot(limit=100): # pragma: no cover
    # We may have already loaded this post, so check title
    existing = Post.query.filter_by(title=submission.title).first() # pragma: no cover
    if existing is None: # pragma: no cover
        link = False # pragma: no cover
        url = None # pragma: no cover
        if ('reddit.com' not in submission.url): # pragma: no cover
            link = True # pragma: no cover
            url = submission.url # pragma: no cover

        p = Post(title=submission.title, # pragma: no cover
                 body=submission.selftext, # pragma: no cover
                 timestamp=datetime.utcfromtimestamp(submission.created_utc), # pragma: no cover
                 vote_count=0, # pragma: no cover
                 link=link, # pragma: no cover
                 url=url, # pragma: no cover
                 user_id=u.id, # pragma: no cover
                 category_id=c.id) # pragma: no cover
        print(f"Creating post: {p} with url {p.url} in {c.title}") # pragma: no cover
        db.session.add(p) # pragma: no cover
        db.session.commit() # pragma: no cover
