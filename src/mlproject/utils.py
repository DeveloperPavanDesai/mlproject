import os
import sys
import logging
from mlproject.exception import CustomException
import pandas as pd 
from dataclasses import dataclass
from dotenv import load_dotenv
import pymysql


load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db,
        )
        logging.info(f'Connection established: {mydb}')

        df = pd.read_sql_query('SELECT * FROM students', mydb)
        return df
    except Exception as e:
        raise CustomException(e, sys)