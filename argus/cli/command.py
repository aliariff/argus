from argus.db.influxdb import InfluxDB
import argus.runners.populate as Populate
import click


@click.group()
def cli():
    InfluxDB()  # init db


@cli.command()
@click.option('--url', default=[])
@click.option('--days', default=1)
def populate(url, days):
    Populate.run(url, days)
