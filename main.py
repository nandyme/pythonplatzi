clients = 'nandy,nelsi,'


def create_client():
	global clients
	new = _get_new_client()
	if new not in clients:
		clients += new
		_add_comma()
	else:
		print('The client is already exist in client list.')


def update_client():
	global clients

	old_client = _get_new_client()
	if old_client in clients:
		client = input('Enter the new name of the client: ')
		clients = clients.replace(old_client + ',', client + ',')
	else:
		print('The client is not in the client list yet.')
		print('Do you want to add it now?')
		selection = input('Select [Y]es or [N]ot: ')
		selection = selection.upper()

		if selection == 'Y':
			clients += old_client
			_add_comma()
		else:
			pass

def del_client():
	global clients
	to_del = _get_new_client()
	if to_del in clients:
		clients = clients.replace(to_del + ',', '')
	else:
		print('The client is not in clients list.')

def welcome():
	print('WELCOME TO PLATZI VENTAS')
	print('*' * 50)
	print('What would yo want to do? ')
	print('[C]reate client')
	print('[U]pdate client')
	print('[D]elete')


def _get_new_client():
	return input('What is the name of the client? ')



def _add_comma(): 
	global clients
	clients += ','


if __name__ == '__main__':
	welcome()
	command = input('Ingress your selection: ')
	command = command.upper()
	
	if command == 'C':
		create_client()
	elif command == 'D':
		del_client()
	elif command == 'U':
		update_client()
	else:
		print('Incorrect command.')

	print(clients)