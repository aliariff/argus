import functools
from influxdb import InfluxDBClient

def client():
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
    client.create_database('example')
    return client
