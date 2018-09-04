import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--urls', default=[])
@click.option('--days', default=1)
def populate(urls, days):
    click.echo(days)
    click.echo(urls)
