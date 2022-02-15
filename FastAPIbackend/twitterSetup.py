from typing import Optional, List
import tweepy
from decouple import config


apikey = config("APIKEY")
apisecret = config("APIKEY_SECRET")
access_token = config("ACCESS_TOKEN")
access_token_secret = config("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(apikey, apisecret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)


def getSpecificUser(user: str, add_rts: Optional[bool] = False, add_replies: Optional[bool] = True, limit: Optional[int]=50):
    try:
        x = api.user_timeline(screen_name=user, include_rts = add_rts, count = limit, exclude_replies = add_replies,trim_user = '')
        # PRINT FOR TESTS
        for t in x:
            print('---------------------------------')
            print(t.full_text)
            print(t.created_at)
            print('---------------------------------')
        # return x
    except:
        return None
    #do something or return it

def gettrending(area: str, limit: Optional[int]=50):
    try:
        x = api.get_place_trends(area)
        y: List[str]
        for p in x[:limit]:
            y.add(p.text)
        return y
    except:
        return None
