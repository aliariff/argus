from influxdb import InfluxDBClient


class InfluxDB(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            db_config = {
                'host': 'localhost',
                'port': 8086,
                'user': 'root',
                'password': 'root',
                'dbname': 'example'
            }
            try:
                print('connecting to InfluxDB database...')
                cls._instance.connection = InfluxDBClient(db_config['host'],
                                                          db_config['port'],
                                                          db_config['user'],
                                                          db_config['password'],
                                                          db_config['dbname'])
                cls._instance.connection.create_database(db_config['dbname'])

            except Exception as error:
                print('Error: connection not established {}'.format(error))

        return cls._instance

    def __init__(self):
        self.connection = self._instance.connection

    def save(self, metrics):
        try:
            self.connection.write_points(metrics)
        except Exception as error:
            print('Error saving metrics "{}", error: {}'.format(metrics, error))
            return None
