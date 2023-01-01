import logging
from geoalchemy2.functions import ST_Point
from datetime import datetime
import db_engine

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("location-api")

def create(loc_message):
    coordinate = ST_Point(
        loc_message['latitude'], loc_message['longitude'])

    add = db_engine.locations.insert().values(
        person_id=loc_message['userId'],
        creation_time=datetime.utcnow(),
        coordinate=coordinate
    )

    with db_engine.db.begin() as conn:
        conn.execute(add)