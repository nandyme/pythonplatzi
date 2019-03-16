import os

clients = [
	#this is the principal list
	{
		'name': 'Pablo',
		'company': 'Google',
		'email': 'pablo@google.com',
		'position': 'Software Engineer'
	},
	{
		'name': 'Ricardo',
		'company': 'Facebook',
		'email': 'ricardo@facebook.com',
		'position': 'Data Engineer'
	}
	]


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


def delete_client(client_name):
	#function called to delete a client
	global clients

	if client_name in clients:
		clients.remove(client_name)
	else:
		print('The client is not in list.')


def searc_client(client_name):
	#function called to search a client in the principal list
	global clients

	client_list = clients.split(',')

	for client in client_list:
		if client != client_name:
			print('The client is in clients list.')
			print('What would you like to do? ')
			_ask_for_modify_clients_list()
			print('[N]othing')
			command = input()
			command = command.upper()
			if command == 'U' :
				update_client(client_name)
			elif command == 'D':
				delete_client(client_name)
			else:
				print('Invalid command.')
		else:
			_client_is_not_in_list(client_name)


def list_clients():
	#function called to print all the clients in the principal list
	global clients

	for idx, client in enumerate(clients):
		print('{uid} | {name} | {company} | {email} | {position}'.format(
			uid = idx ,
			name = client['name'],
			company = client['company'],
			email = client['email'],
			position = client['position']))


"""def _client_is_not_in_list(client_name):
	#function called when the client's dictionary is not in list, to ask if you want to do
	#something with the dictionary received
	print('Client is not in clients list.')
	print('Do you want to add it now? ')
	selection = _yes_or_not()
	if selection == 'Y':
		create_client(client_name)
	else:
		pass


def _yes_or_not():
	#returns a selection command Y or N in a string
	selection = input('[Y]es or [N]ot: ')
	selection = selection.upper()
	return selection"""


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


if __name__ == '__main__':
	_print_welcome()

	command = input()
	command = command.upper()

	if command == 'C':
		client = {
							'name': _get_client_field('name'),
							'company': _get_client_field('company'),
							'email': _get_client_field('email'),
							'position': _get_client_field('position')
				}
		create_client(client)
		list_clients()
	elif command == 'L':
		list_clients()
	elif command == 'D':
		delete_client(_get_client_field())
		list_clients()
	elif command == 'U':
		uname = input('Ingress the name of the client that you want to update: ')
		update_client(uname)
		list_clients()
	elif command == 'S':
		searc_client(_get_client_field())
		list_clients()
	elif command == 'L':
		list_clients()
	else:
		print('Invalid command.')

	os.system('pause')