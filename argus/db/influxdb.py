import coloredlogs
import logging
from influxdb import InfluxDBClient

logger = logging.getLogger(__name__)
coloredlogs.install()


class InfluxDB(object):
    _instance = None

    def __new__(cls, db_config=None):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            try:
                logging.info("connecting to InfluxDB database...")
                cls._instance.connection = InfluxDBClient(**db_config)
                cls._instance.connection.create_database(db_config["database"])
            except Exception as error:
                logging.error("Error: connection not established {}".format(error))
                raise error

        return cls._instance

    def __init__(self, db_config=None):
        self.connection = self._instance.connection

    def save(self, metrics):
        try:
            self.connection.write_points(metrics)
        except Exception as error:
            logging.error('Error saving metrics "{}", error: {}'.format(metrics, error))
            return None
