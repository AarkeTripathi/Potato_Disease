from fastapi import FastAPI
from enum import Enum

app=FastAPI()

class Available_cuisines(str, Enum):
    indian='indian'
    mexican='mexican'
    chinese='chinese'

@app.get('/hello/{cuisine}')
#async method lets another request be accepted while the first ine is being processed in case there are multiple requests
async def hello(cuisine: Available_cuisines):     #this ':' is feature provided by fastapi to provide validation on the cuisine variable(basically the values can only be the values in the available_cuisines datatype defined by the class Available_cuisines) 
    return f'{cuisine} is available'