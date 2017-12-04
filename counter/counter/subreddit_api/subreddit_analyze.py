import praw
import json
import os

from counter.settings_secret import *

reddit = praw.Reddit(
        client_id = REDDIT_CLIENT_ID, 
        client_secret = REDDIT_CLIENT_SECRET , 
        user_agent = "my user agent")

DEFAULT_CHAR_TO_COUNT = 'p'

def count_char(text, character = DEFAULT_CHAR_TO_COUNT):
    return text.lower().count(character)

def aggregate_counts(result):
    total = result[ "display_name" ] + result[ "title" ] + result[ "description" ]

    for key,post in result[ "posts" ].items():
        total += post[ "title" ] + post[ "comments" ] + post[ "url" ]

    return total

# Analyzes the character count in comments of a given post
def analyze_comments(id):
    submission = reddit.submission(id=id)

    submission.comments.replace_more(limit=None) # expand all comments

    comment_result = 0
    for comment in submission.comments.list():
        comment_result += count_char(comment.body)

    return { "post_id" : id , "total_count" : comment_result ,
            "comments_link" : "https://www.reddit.com/r/facepalm/comments/" + id }

# Analyzes the character count for a given post under a subreddit
def analyze_post(post, full_url):
    post_result = {};
    post_result[ "id" ] = post.id
    post_result[ "title" ] = post.title
    post_result[ "url" ] = post.url
    post_result[ "id_count" ] = count_char( post.id )
    post_result[ "title_count" ] = count_char( post.title )
    post_result[ "url_count" ] = count_char( post.url )
    # post_result[ "comments_count" ] = analyze_comments( post.id )

    # generate a link to access comments info
    post_result[ "comments_info" ] = full_url + "/" + post.id + "/comments_info"
    return post_result
    
def analyze_posts(subreddit, full_url, params = {}):
    posts_result = []

    count = 0
    for post in subreddit.hot(limit= params["limit"] ):
        # print( "processing post ", count )
        count += 1
        posts_result.append( analyze_post(post, full_url) )

    return posts_result

# Analyzes the character count for a given subreddit
def analyze_subreddit(subreddit_name, full_url, params={}):
    result = {}
    subreddit = reddit.subreddit(subreddit_name)

    result[ "display_name" ] = subreddit.display_name
    result[ "title" ] = subreddit.title

    result[ "display_name_count" ] = count_char( subreddit.display_name )
    result[ "title_count" ] = count_char( subreddit.title )
    result[ "description_count" ] = count_char( subreddit.description )
    result[ "posts" ] = analyze_posts( subreddit , full_url, params)

    return result
