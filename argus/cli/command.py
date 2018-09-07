from argus.db.influxdb import InfluxDB
import argus.runners.populate as Populate
import click


@click.group()
@click.option('--host', default='localhost:8086')
@click.option('--user', default='root')
@click.option('--password', default='root')
@click.option('--db', default='example')
def cli(host, user, password, db):
    host, port = host.split(':')
    db_config = {
        'host': host,
        'port': port,
        'username': user,
        'password': password,
        'database': db
    }
    InfluxDB(db_config)


@cli.command()
@click.option('--url', default='')
@click.option('--days', default=1)
def populate(url, days):
    Populate.run(url, days)
