import click

from clients.services import ClientService
from clients.models import Client

@click.group()
def clients(ctx):
	"""Manages the clients lifecycle"""
	pass

@clients.command()
@click.option('-n', '--name',
				type = str,
				prompt = True,
				help = 'The client\'s name')
@click.option('-c', '--company',
				type = str,
				prompt = True,
				help = 'The client\'s company')
@click.option('-e', '--email',
				type = str,
				prompt = True,
				help = 'The client\'s email')
@click.option('-p', '--position',
				type = str,
				prompt = True,
				help = 'The client\'s position')
@click.pass_context
def create(ctx, name, company, email, position):
	"""Creates a new client"""
	client = Client(name, company, email, position)
	client_service = ClientService(ctx.obj['clients_table'])
	
	client_service.create_client(client)


@clients.command()
@click.pass_context
def update(ctx):
	"""Updates a client"""
	pass


@clients.command()
@click.pass_context
def delete(ctx):
	"""Deletes a client"""
	pass


all = clients
