

clients = 'sergio,jorge,ruben,'


def create_client(client_name):
	global clients
	
	if client_name not in clients:
		clients += client_name
		_add_comma()
	else:
		print('That client already is in clients list.')




def update_client(client_name):
	global clients


	if client_name in clients:
		updated_client_name = input('What is the new name for the client? ')
		clients = clients.replace(client_name + ',', updated_client_name + ',')
	else:
		_client_is_not_in_list(client_name)


def delete_client(client_name):
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',','')
	else:
		_client_is_not_in_list()


def searc_client(client_name):
	global clients

	if client_name in clients:
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
			pass
	else:
		_client_is_not_in_list(client_name)


def _add_comma():
	global clients

	clients += ','


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

def _get_client_name():
	return input('What is the client name? ')


def list_clients():
	global clients

	print(clients)

def _print_welcome():
	print('WELCOME TO PLATZI VENTAS')
	print('*' * 50)
	print('What would you like to do? ')
	print('[C]reate client')
	_ask_for_modify_clients_list()
	print('[S]earch client')


def _ask_for_modify_clients_list():
	print('[U]pdate client')
	print('[D]elete client')


if __name__ == '__main__':
	_print_welcome()

	command = input()
	command = command.upper()

	if command == 'C':
		client_name = _get_client_name()
		create_client(client_name)
		list_clients()
	elif command == 'D':
		delete_client(_get_client_name())
	elif command == 'U':
		update_client(_get_client_name())
	elif command == 'S':
		searc_client(_get_client_name())
	else:
		print('Invalid command.')

	
	list_clients()