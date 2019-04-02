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
	#function called to append a client's dictionary to the principal list.
	global clients
	switch = True #this variable will be changed for False if the client is already in the list.
	
	for i in clients:
		if i['name'] == client['name']:
			switch = False
		else:
			pass

	if switch:
		clients.append(client)
		os.system('cls')
		_print_results('The client {} has been created successfully'.format(client['name']))
	else:
		os.system('cls')
		_print_results('That client can\'t be created.\nIt\'s already in the list.')


def update_client(uname):
	#function called to modify one client's data.
	global clients
	switch = False #this variable is kept false if the client is not in the list.

	for client in clients:
		uname = uname.capitalize()
		if client['name'] == uname:
			switch = True #comes to true if the client is in the list.
			ukey = input('What do you want to update from this client?\n(Name, Company, Email, Position): ')
			ukey.lower()
			client[ukey] = (input('Ingress the new {} of the client: '.format(ukey))).capitalize()
			client['email'] = client['email'].lower()
			os.system('cls')
			_print_results('The client {} has been updated successfully'.format(uname))
			break
		else:
			pass
	if not switch:
			os.system('cls')
			_print_results('The client is not in the clients list.')


def delete_client(uname):
	#function called to delete a client.
	global clients
	switch = False

	for client in clients:
		if client['name'] == uname:
			switch = True
			clients.remove(client)
			os.system('cls')
			_print_results('The client {} has been deleted successfully.'.format(client['name']))
		else:
			pass

	if not switch:
		os.system('cls')
		_print_results('The client is not in list.')

def search_client(uname):
	#function called to search a client in the principal list.
	global clients
	uname = uname.capitalize()
	switch = False #this variable is kept false if the client is not in the list.

	for client in clients:
		if client['name'] == uname:
			switch = True #comes to true if the client is in the list.
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
				_print_results('Invalid command.')
		else:
			pass
	if not switch:
		_print_results('The client is not in list.')


def list_clients():
	#function called to print all the clients in the principal list.
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


def _print_results(results):
	#prints the final results prettier ;)
	print('*'*70)
	print(' '*(35-(len(results)//2))+results+' '*(35-(len(results)//2)))
	print('*'*70)



def _print_welcome():
	#shows to the user all the options he have
	print('WELCOME TO PLATZI VENTAS')
	print('*' * 50)
	print('What would you like to do? ')
	print('[C]reate client')
	print('[L]ist clients')
	_ask_for_modify_clients_list()
	print('[S]earch client')


def _ask_for_modify_clients_list():
	#part of the options that will showed in _print_welcome
	print('[U]pdate client')
	print('[D]elete client')


def get_client_key(ukey):
	os.system('cls')
	return input('Ingress the name of the client that you want to '+ukey+': ')


if __name__ == '__main__':
	_initialize_clients_from_storage()
	_print_welcome()

	command = input()
	command = command.upper()

	if command == 'C':
		os.system('cls')
		client = {
							'name': _get_client_field('name').capitalize(),
							'company': _get_client_field('company').capitalize(),
							'email': _get_client_field('email'),
							'position': _get_client_field('position').capitalize()
				}
		create_client(client)
	elif command == 'L':
		os.system('cls')
		list_clients()
	elif command == 'D':
		delete_client(get_client_key('delete').capitalize())
	elif command == 'U':
		update_client(get_client_key('update').capitalize())
	elif command == 'S':
		search_client(get_client_key('search').capitalize())
	else:
		os.system('cls')
		print('Invalid command.')


	_save_clients_to_storage()
	print('')
	print('')
	print('')
	os.system('pause')