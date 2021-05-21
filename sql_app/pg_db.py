import databases, sqlalchemy
import datetime, random, uuid
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String ,DateTime ,Boolean
from databases import DatabaseURL
from starlette.config import Config
from starlette.datastructures import Secret

# config

config = Config("./../.env")

POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str)

# connect to database
DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# define table
users = sqlalchemy.Table(
    'result',
    metadata,
    sqlalchemy.Column('user_id' , String, primary_key = True),
    sqlalchemy.Column('news_url', String, primary_key = True),
    sqlalchemy.Column('comment', String),
    sqlalchemy.Column('create_at', DateTime, default = datetime.datetime.utcnow),
    sqlalchemy.Column('news_result', Boolean),
    sqlalchemy.Column('block_chain_url', String)
)

engine = create_engine(
    DATABASE_URL
)
metadata.create_all(engine)
