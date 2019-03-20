import os
import csv

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients =[]

def _initialize_clients_from_storage():
	with open(CLIENT_TABLE, mode = 'r') as f:
		reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

		for row in reader:
			clients.append(row)


def _save_clients_to_storage():
	tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
	with open(tmp_table_name, mode = 'w') as f:
		writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
		writer.writerows(clients)

	os.remove(CLIENT_TABLE)
	os.rename(tmp_table_name, CLIENT_TABLE) 


def create_client(client):
	#function called to append a client's dictionary to the principal list
	global clients
	
	if client not in clients:
		clients.append(client)
	else:
		print('That client already is in clients list.')


def update_client(uname):
	#function called to modify one client's data
	global clients

	for client in clients:
		uname = uname.capitalize()
		if client['name'] == uname:
			ukey = input('What to you want to update from this client?\n(Name, Company, Email, Position): ')
			ukey.lower()
			client[ukey] = (input('Ingress the new {} of the client: '.format(ukey))).capitalize()
			client['email'] = client['email'].lower()
			break
			"""if ukey != 'email':
													client[ukey] = (input('Ingress the new {} of the client: '.format(ukey))).capitalize()
													break
												else:
													client[ukey] = input('Ingress the new {} of the client: '.format(ukey))
													break"""
		else:
			print('The client is not in the clients list.')


def delete_client(uname):
	#function called to delete a client
	global clients

	for client in clients:
		if client['name'] == uname:
			clients.remove(client)
		else:
			print('The client is not in list.')


def searc_client(uname):
	#function called to search a client in the principal list
	global clients

	for client in clients:
		if client['name'] == uname:
			print('The client is in clients list.')
			print('What would you like to do? ')
			_ask_for_modify_clients_list()
			print('[N]othing')
			command = input()
			command = command.upper()
			if command == 'U' :
				update_client(uname)
			elif command == 'D':
				delete_client(uname)
			else:
				print('Invalid command.')
		else:
			print('Client is not in list.')


def list_clients():
	#function called to print all the clients in the principal list
	global clients

	for idx, client in enumerate(clients):
		print('{uid} | {name} | {company} | {email} | {position}'.format(
			uid = idx,
			name = client['name'],
			company = client['company'],
			email = client['email'],
			position = client['position']))



def _get_client_field(data):
	#returns a data to complete a the field in the dictionary below
	field = None

	while not field:
		field = input('What is the client {}?'.format(data))
	return field


def _print_welcome():
	#shows to the user all the options he have
	print('WELCOME TO PLATZI VENTAS')
	print('*' * 50)
	print('What would you like to do? ')
	print('[C]reate client')
	print('[L]ist clients')
	_ask_for_modify_clients_list()
	print('[S]earch client')
	print('[L]ist clients')


def _ask_for_modify_clients_list():
	#part of the options that will showed in _print_welcome
	print('[U]pdate client')
	print('[D]elete client')


def get_client_key(ukey):
	return input('Ingress the name of the client that you want to '+ukey+': ')


if __name__ == '__main__':
	_initialize_clients_from_storage()
	_print_welcome()

	command = input()
	command = command.upper()

	if command == 'C':
		client = {
							'name': _get_client_field('name').capitalize(),
							'company': _get_client_field('company').capitalize(),
							'email': _get_client_field('email'),
							'position': _get_client_field('position').capitalize()
				}
		create_client(client)
	elif command == 'L':
		list_clients()
	elif command == 'D':
		delete_client(get_client_key('delete').capitalize())
	elif command == 'U':
		update_client(get_client_key('update').capitalize())
	elif command == 'S':
		searc_client(get_client_key('search').capitalize())
	else:
		print('Invalid command.')


	_save_clients_to_storage()