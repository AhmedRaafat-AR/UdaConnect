import os
from sqlalchemy import create_engine, MetaData


DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]


db = create_engine(
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

metadata_obj = MetaData()
metadata_obj.reflect(bind=db)
locations = metadata_obj.tables['location']