from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String ,DateTime ,Boolean
from typing import List, Optional
import datetime, random, uuid

# body
import pg_db
import model
database = pg_db.database
users = pg_db.users

# enable CORS
origins = [
    "*"
]

# fastapi
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

@app.get('/users', response_model = List[model.UserList], status_code = 202)
async def find_all_user():
    query = users.select()
    return await database.fetch_all(query)

@app.post('/users/{user_id}/{news_url}/{news_result}', status_code = 201)
async def register_user(user : model.UserEntry):
    gDate = datetime.datetime.now()
    try :
        query = users.insert().values(
            user_id = user.user_id,
            news_url = user.news_url,
            create_at = gDate,
            news_result = user.news_result
        )
        await database.execute(query)
        return {
            'user_id'          : user.user_id,
            'news_url'         : user.news_url,
            'news_result'      : user.news_result,
        }
    except :
        return JSONResponse(status_code=409, content={"message": "Item already exists."})


@app.get('/users/{user_id}/{news_url}', response_model = model.UserListGetid)
async def find_user_by_id(user_id : str, news_url : str):
    query = users.select().where(users.c.user_id == user_id ).where( users.c.news_url == news_url )
    return await database.fetch_one(query)

@app.put('/users', response_model = model.UserList)
async def update_user(user : model.UserUpdate):
    gDate = datetime.datetime.now()
    query = users.update().\
        where(users.c.user_id == user.user_id and users.c.news_url == user.news_url).\
        values(
            create_at = gDate,
            news_result = user.news_result,
            block_chain_url = user.block_chain_url
        )
    await database.execute(query)

    return await find_user_by_id(user_id= user.user_id, news_url =  user.news_url)

@app.delete('/users/{user_id}/{news_url}')
async def delete_user(user: model.UserDelete):
    query = users.delete().where(users.c.user_id == user.user_id ).where( users.c.news_url == user.news_url )
    await database.execute(query)

    return {
        'message': 'This user has been deleted successfully'
    }
