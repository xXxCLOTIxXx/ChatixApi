from client import Client
import time

adminId = 'admin code'
name = 'bot name'

client = Client(name=name)
old_message = []
def on_msg():
	while True:
		time.sleep(0.2)
		json = client.getChatJson(adminId=adminId).json()
		for i in range(len(json['chat'])):
			message = json['chat'][i]['message']
			name = json['chat'][i]['name']
			messageId = json['chat'][i]['messageId']
			userId = json['chat'][i]['uid']
			ct = f'{name}: {message}'
			content =  message.split()
			if f'{ct}: {messageId}' not in old_message:
				old_message.append(f'{ct}: {messageId}')
				print(ct)
				if content[0][0] == '/':
					if content[0][1:].lower() == 'ping':
						client.send_message(message='Pong!')
					elif content[0][1:].lower() == 'pong':
						client.send_message(message='Ping!')

if __name__ == '__main__':
	on_msg()