import praw
import json
import os
reddit = praw.Reddit(
        client_id = os.environ["REDDIT_CLIENT_ID"], 
        client_secret = os.environ["REDDIT_CLIENT_SECRET"] , 
        user_agent = "my user agent")

DEFAULT_CHAR_TO_COUNT = 'p'

def count_char(text, character = DEFAULT_CHAR_TO_COUNT):
    return text.lower().count(character)

def aggregate_counts(result):
    total = result[ "display_name" ] + result[ "title" ] + result[ "description" ]

    for key,post in result[ "posts" ].items():
        total += post[ "title" ] + post[ "comments" ] + post[ "url" ]

    return total

# Analyzes the character count for a given post under a subreddit
def analyze_comments(id):
    submission = reddit.submission(id=id)

    submission.comments.replace_more(limit=None) # expand all comments
    # submission.comments.replace_more(limit=0) # remove MoreComments

    comment_result = 0

    for comment in submission.comments.list():
        comment_result += count_char(comment.body)

    return comment_result

# Analyzes the character count for a given post under a subreddit
def analyze_posts(subreddit):
    post_result = {}

    # limit = 3
    limit = None

    count = 0
    for post in subreddit.hot(limit=limit):
        print( "processing post ", count )
        count += 1

        post_result[ post.id ] = {}
        post_result[ post.id ][ "title" ] = count_char( post.title )
        post_result[ post.id ][ "url" ] = count_char( post.url )
        # post_result[ post.id ][ "comments" ] = analyze_comments( post.id )

    return post_result

# Analyzes the character count for a given subreddit
def analyze(subreddit_name):
    result = {}
    subreddit = reddit.subreddit(subreddit_name)

    result[ "display_name" ] = subreddit.display_name
    result[ "title" ] = subreddit.title

    result[ "display_name_count" ] = count_char( subreddit.display_name )
    result[ "title_count" ] = count_char( subreddit.title )
    result[ "description_count" ] = count_char( subreddit.description )
    # result[ "posts" ] = analyze_posts( subreddit )

    return result

# p_count_breakdown = analyze( 'facepalm' )
# result = {
#     "p_count_breakdown" : p_count_breakdown,
#     "total_p_count" : aggregate_counts( p_count_breakdown )
#     }
