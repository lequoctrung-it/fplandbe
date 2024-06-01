import os

import psycopg2
from sqlalchemy import create_engine
from dotenv import load_dotenv


def create_db_conn():
    load_dotenv()

    db_config = {
        'database': os.environ['DB_NAME'],
        'user': os.environ['DB_USER'],
        'password': os.environ['DB_PASSWORD'],
        'host': os.environ['DB_HOST'],
        'port': os.environ['DB_PORT'],
    }

    conn = psycopg2.connect(**db_config)
    db_url = (f'postgresql+psycopg2://{db_config["user"]}:{db_config["password"]}'
              f'@{db_config["host"]}:{db_config["port"]}/{db_config["database"]}')
    engine = create_engine(db_url)

    return conn, engine
