import json
import click
import logging
from flask.cli import FlaskGroup

from bard_api.models import Collection
from bard_api.app import create_app
from bard_api.migration import upgrade_system

log = logging.getLogger("bard")

@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    pass

@cli.command()
def upgrade():
    log.info("upgrade")
    upgrade_system()