import requests
import api
import exceptions
import generator
import __init__

class Client():
	__init__.init()

	def __init__(self, name: str = None):
		if name == None:
			print('Error name');exit()
		else:
			self.name = name
		self.uid = generator.generateUid()



	def getChatMessages(self, amount: int = None):

		"""
		**Parameters**

		 'amount' - Number of messages

		"""

		response = requests.get(f'{api.api}{api.getMessageApi}?amount={amount}')
		if response.status_code != 200:
			return exceptions.CheckException(response.text)
		else:
			return response

	def getChatJson(self, adminId: str = None):

		"""
		**Parameters**

		'adminId' - Administration code for receiving a response from the server

		"""

		response = requests.get(f'{api.api}{api.getJsonChatApi}?adminId={adminId}&name={self.name}&uid={self.uid}')
		if response.status_code != 200:
			return exceptions.CheckException(response.text)
		else:
			return response
	def send_message(self, message: str = None, replyTo: str = None, fileUrl: str = None, adminId: str = None, file = None):

		"""
		**Parameters**

		'message' - Message to send

		'replyTo' - reply to message (not working yet)

		'fileUrl' - link to file to send

		'adminId' - Administration code for receiving a response from the server
		

		"""
		if fileUrl != None:
			self.data = {'url': fileUrl}
			response = requests.post(f'{api.api}{api.sendFileUrlApi}?name={self.name}&adminId={adminId}&uid={self.uid}', data=self.data)
		elif message != None:
			response = requests.get(f'{api.api}{api.sendMessageApi}?name={self.name}&message={message}&replyTo={replyTo}&adminId={adminId}&uid={self.uid}')
		elif file != None:
			return 'not working yet'
		else:
			return 'Enter a message or a link to an image'
		if response.status_code != 200:
			return exceptions.CheckException(response.text)
		else:
			return response


	def clearChat(self, adminId: str):

		"""
		**Parameters**

		'adminId' - Administration code for receiving a response from the server

		"""
		response = requests.get(f'{api.api}{api.clearChatApi}?name={self.name}&adminId={adminId}&uid={self.uid}')
		if response.status_code != 200:
			return exceptions.CheckException(response.text)
		else:
			return response


	def onlyViewMode(self, adminId: str, viewMode: str):

		"""
		**Parameters**

		'adminId' - Administration code for receiving a response from the server

		'viewMode' - on or off

		"""
		response = requests.get(f'{api.api}{api.ViewModeApi}?name={self.name}&adminId={adminId}&uid={self.uid}&onlyView={viewMode}')
		if response.status_code != 200:
			return exceptions.CheckException(response.text)
		else:
			return response

	def getUid(self, adminId: str):
		"""
		**Parameters**

		'adminId' - Administration code for receiving a response from the server

		"""

		response = requests.get(f'{api.api}{api.getUidApi}?name={self.name}&adminId={adminId}&uid={self.uid}')

		if response.status_code != 200:
			return exceptions.CheckException(response.text)
		else:
			return response.text.replace("<br>", "\n").replace("<p>", "")


	def edit_background(self, adminId: str, imgUrl: str = None, file=None):
		"""
		**Parameters**

		'adminId' - Administration code for receiving a response from the server

		'imgUrl' - Link to picture

		'file' - Picture file

		"""



		if imgUrl != None:
			self.data = {'url': imgUrl}
			response = requests.post(f'{api.api}{api.updateBackgroundApi}?name={self.name}&adminId={adminId}&uid={self.uid}', data=self.data)
		elif file !=None:
			return 'not working yet'
		else:
			return 'Enter a file or a link to an image'

		if response.status_code != 200:
			return exceptions.CheckException(response.text)
		else:
			return response


	#=======================not working yet=========================

	def ban(self, adminId: str, userId: str):


		"""
		**Parameters**

		'adminId' - Administration code for receiving a response from the server

		'userId' - ID of the user you want to ban

		"""

		response = requests.get(f'{api.api}{api.BanApi}?name={self.name}&adminId={adminId}&uid={self.uid}&banUid={userId}')

		if response.status_code != 200:
			return exceptions.CheckException(response.text)
		else:
			return response


	def unban(self, adminId: str, userId: str):

		"""
		**Parameters**

		'adminId' - Administration code for receiving a response from the server

		'userId' - ID of the user you want to unban

		"""


		response = requests.get(f'{api.api}{api.unBanApi}?name={self.name}&adminId={adminId}&uid={self.uid}&unbanUid={userId}')

		if response.status_code != 200:
			return exceptions.CheckException(response.text)
		else:
			return response