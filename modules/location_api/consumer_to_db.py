import logging
from geoalchemy2.functions import ST_Point
from ast import Dict
from models import Location
from schemas import LocationSchema
from geoalchemy2.functions import ST_Point
from db_engine import db_engine

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("location-api")

def consumer_to_db(location_message):
    @staticmethod
    def create(location: Dict) -> Location:
        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            logger.warning(f"Unexpected data format in payload: {validation_results}")
            raise Exception(f"Invalid payload: {validation_results}")

        new_location = Location()
        new_location.person_id = location["userId"]
        new_location.creation_time = location["creation_time"]
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        db_engine.db.session.add(new_location)
        db_engine.db.session.commit()

        return new_location