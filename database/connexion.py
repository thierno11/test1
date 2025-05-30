from psycopg2 import connect
from dotenv import load_dotenv
import os
from psycopg2.extras import RealDictCursor
from .script import USER

load_dotenv()

conn = connect(
    database=os.getenv("DATABASE_NAME"),
    user=os.getenv("DATABASE_USER"),
    password = os.getenv("DATABASE_PASSWORD"),
    port=os.getenv("DATABASE_PORT"),
    host=os.getenv("DATABASE_HOST"),
    cursor_factory=RealDictCursor
    )


# creation 

def get_db():
    try:
        cursor = conn.cursor()
        yield cursor
    finally:
        cursor.connection.commit()
        cursor.close()

def initialisation():
    try:
        cursor=conn.cursor()
        cursor.execute(USER)
        cursor.connection.commit()
        cursor.close()
    except Exception as e:
        print(e)
    