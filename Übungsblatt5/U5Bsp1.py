"""
Gregor Wagner
U5Bsp1.py - small tweets, Big Data analysis
Gregor Wagner, 52005240
"""
import json
import re
from collections import Counter

class Tweet():
    def __init__(self, time, message, user):
        self.time = time
        self.message = message
        self.user = user.split("/")[-1]

def readTweets(tweets):
    f = open("twitter_small.json", mode="r", encoding="utf=8")
    twitter_data = json.load(f)
    f.close

    for t in twitter_data['tweets'] :
        tweets.append(Tweet(t['time'], t['message'].lower(), t['user']))


def listCommands(commands):
    print("Usage: allowed keywords are: ")
    for key, value in commands.items() :
        print(f"\t{key} {value.__name__}")
    print("\texit")
    print("help for Usage")

def tweet_count(tweets):
    print(f"Anzahl der Tweets: {len(tweets)}")

def top_hashtags(tweets):
    pattern = '#\w*'
    hashtags = []
    for t in tweets :
        if "#" in t.message :
            hashtags.extend(re.findall(pattern, t.message))
    print(f"Top 5 Hashtags:  {Counter(hashtags).most_common(5)}")

def top_users(tweets):
    users = []
    for t in tweets :
        users.append(t.user)
    print(f"Top 5 Users: {Counter(users).most_common(5)}")

def top_tweet_day(tweets):
    tweetsInDays = []
    for t in tweets :
        tweetsInDays.append(t.time.split(" ")[0])
    print(f"Top Tage an denen gepostet wurde: {Counter(tweetsInDays).most_common(5)}")


def top_hashtag_user(tweets):
    pass

def main():
    tweets = []

    commands = {"1" : tweet_count,
                "2" : top_hashtags,
                "3" : top_users, 
                "4" : top_tweet_day, 
                "5" : top_hashtag_user}


    listCommands(commands)
    
    readTweets(tweets)
    print("\nTweets successfully imported\n")

    print("------------------------")
    while (consoleLog := input("Keyword --> ")) != "exit" :
        command = consoleLog.lower()
        for key, value in commands.items() :
            if command == key.lower() :
                value(tweets)
                print("------------------------")
            
        if command not in commands :
            listCommands(commands)


if __name__ == "__main__":
    main()