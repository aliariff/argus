import click
import argus.runners.populate as Populate


@click.group()
def cli():
    pass


@cli.command()
@click.option('--url', default=[])
@click.option('--days', default=1)
def populate(url, days):
    Populate.run(url, days)
