import databases, sqlalchemy
import datetime, random, uuid
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String ,DateTime ,Boolean

#connect to database
DATABASE_URL = 'postgresql://kjyang:netdb2602@localhost:5432/news_postgres'
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

#define table
users = sqlalchemy.Table(
    'result',
    metadata,
    sqlalchemy.Column('user_id' , String, primary_key = True),
    sqlalchemy.Column('news_url', String, primary_key = True),
    sqlalchemy.Column('create_at', DateTime, default = datetime.datetime.utcnow),
    sqlalchemy.Column('news_result', Boolean),
    sqlalchemy.Column('block_chain_url', String),
)

engine = create_engine(
    DATABASE_URL
)
metadata.create_all(engine)
