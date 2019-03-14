

clients = [
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
	global clients
	
	if client not in clients:
		clients.append(client)
	else:
		print('That client already is in clients list.')


<<<<<<< HEAD
yield


=======
>>>>>>> a51cfdbfca9516c3f65d38ca4d787ab842e2cd3d
def update_client(client_name):
	global clients

	if client_name in clients:
		index = clients.index(client_name)
		clients[index] = input('What is the new name for the client? ')
	else:
		_client_is_not_in_list(client_name)


def delete_client(client_name):
	global clients

	if client_name in clients:
		clients.remove(client_name)
	else:
		print('The client is not in list.')


def searc_client(client_name):
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
	global clients

	for idx, client in enumerate(clients):
		print('{}: {}'.format(idx, client))


def _client_is_not_in_list(client_name):
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
	return selection

<<<<<<< HEAD
def _get_client_name():
	client_name = None
	while not client_name:
		client_name = input('What is the client name? ')
	return client_name
=======

def _get_client_field(data):
	field = None
>>>>>>> a51cfdbfca9516c3f65d38ca4d787ab842e2cd3d

	while not field:
		field = input('What is the client {}?'.format(data))
	return field


def _print_welcome():
	print('WELCOME TO PLATZI VENTAS')
	print('*' * 50)
	print('What would you like to do? ')
	print('[C]reate client')
	print('[L]ist clients')
	_ask_for_modify_clients_list()
	print('[S]earch client')
	print('[L]ist clients')


def _ask_for_modify_clients_list():
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
		delete_client(_get_client_name())
		list_clients()
	elif command == 'U':
		update_client(_get_client_name())
		list_clients()
	elif command == 'S':
		searc_client(_get_client_name())
		list_clients()
<<<<<<< HEAD
=======
	elif command == 'L':
		list_clients()
>>>>>>> a51cfdbfca9516c3f65d38ca4d787ab842e2cd3d
	else:
		print('Invalid command.')