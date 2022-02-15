from fastapi import FastAPI
from FastAPIbackend.twitterSetup import getSpecificUser, gettrending
from twitterSetup import *


app = FastAPI()

@app.get('/')
def enter():
    return "Asay Akwaaba to the api"


@app.get('/api/v1/trending')
async def gettrends(limit: int, area:str):
    return gettrending(area,limit)


@app.get('/api/v1/specifics')
async def specifiusertweet(username: str,):
    return getSpecificUser(username)