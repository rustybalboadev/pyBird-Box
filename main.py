import time
import tweepy
import json
import pprint
import github
import os
import crayons
os.system('cls')
upload_amount = 0
API_KEY = '' #Twitter API KEY
API_Secret = '' #Twitter API Secret
ACCESS_TOKEN = '' #Twitter Access Token
ACCESS_TOKEN_SECRET = '' #Twitter Access Secret
ghub_token = '' #Github token
gist_id = '' #Github Gist ID
gh = github.Github(ghub_token)
gist = gh.get_gist(gist_id)
auth = tweepy.OAuthHandler(API_KEY, API_Secret)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
while True:
    timelineList = api.user_timeline(id='YOURTWITTERID', count=1)
    timeline = timelineList[0]
    json_str = json.dumps(timeline._json)
    json_str = json.loads(json_str)
    like_amount = str(json_str['favorite_count'])
    retweet_amount = str(json_str['retweet_count'])
    title = "@YOUR@HERE - ❤️{}|↪️{}".format(like_amount, retweet_amount)
    content = str(json_str['text'])
    final_content = """"""
    i = 0
    for each in content:
        final_content += each
        if i == 55:
            final_content += '\n'
        i += 1
    last_title = str(gist.files).split("'")[1]
    gist.edit(
        files={last_title:github.InputFileContent(content=final_content, new_name=title)},
    )
    upload_amount += 1
    os.system('cls')
    print(crayons.red("""
    Updated!
    Title: {}
    Content: {}
    Time Wait: 15 min 
    Upload Count: {}
    """.format(title, content, upload_amount)))
    time.sleep(15 * 60)

