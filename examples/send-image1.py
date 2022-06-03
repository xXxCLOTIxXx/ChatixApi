from client import Client
import time
name = 'Bot name'
fileUrl = 'link'

client = Client(name=name)
client.send_message(fileUrl=fileUrl)
