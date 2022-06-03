from client import Client
import time
name = 'Bot name'
fileUrl = 'link'

client = Client(name=name)
def on_msg():
	client.send_message(fileUrl=fileUrl)

if __name__ == '__main__':
	on_msg()