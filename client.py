import user
import json
import socket as sk

def get_uris(server, port):
	'''Function that connects to the "dns" uri server
	and find out what chats there are'''
	socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
	socket.connect((server, port))

	socket.send('GET uri'.encode())

	serialized = socket.recv(4096).decode('utf-8')

	return json.loads(serialized)

def main(server='localhost', port=25500):

	#to find a valid username
	while True:
		username = input('Username: ')

		if ':' not in username:
			break
		else:
			print("Nome de usuario não pode ter ':'. tente novamente")


	uris = get_uris(server, port)

	#valid chatroom check
	while True:
		print('Chats rooms:')
		for n, item in enumerate(uris):
			print(f"{n}: {item[0]}")

		selection = input("Pick a chat: ")

		try:
			uri = uris[int(selection)][1]
			break
		except (IndexError, ValueError):
			print(f"'{selection}' is not a valid chat, please, try again.")
	u = user.User(uri, username)


if __name__ == '__main__':
	main()
