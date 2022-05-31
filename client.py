import requests
import api
import exceptions
import __init__

class Client():
	print(__init__.init())


	def getChatMessages(self, amount: int = 99*99*99*99):

		"""
		**Parameters**

		 'amount' - Number of messages

		"""

		response = requests.get(f'{api.api}{api.getMessage}?amount={amount}')
		if response.status_code != 200:
			return exceptions.CheckException(response.text)
		else:
			return response

	def getChatJson(self, adminId: str = None):

		"""
		**Parameters**

		'adminId' - Administration code for receiving a response from the server

		"""

		response = requests.get(f'{api.api}{api.getJsonChat}?adminId={adminId}')
		if response.status_code != 200:
			return exceptions.CheckException(response.text)
		else:
			return response
	def send_message(self, name: str, message: str = None, replyTo: str = None, photoUrl: str = None):

		"""
		**Parameters**

		'name' - Sender name

		'message' - Message to send

		'replyTo' - reply to message (not working yet)

		'photoUrl' - link to picture to send
		

		"""
		if photoUrl != None:
			response = requests.get(f'{api.api}{api.sendPhoto}?name={name}&photoUrl={photoUrl}')
		elif message != None:
			response = requests.get(f'{api.api}{api.sendMessage}?name={name}&message={message}&replyTo={replyTo}')
		else:
			return 'Enter a message or a link to an image'
		if response.status_code != 200:
			return exceptions.CheckException(response.text)
		else:
			return response