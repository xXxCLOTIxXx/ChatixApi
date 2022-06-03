from client import Client
import time
name='Bot Name'
adminId = '35aecb81-8815-47c4-9b65-a0e37550ae24'
client = Client(name=name)


"""
*clear chat*

client.clearChat(adminId=adminId)
"""




"""
*Edit view-only mode*


client.onlyViewMode(adminId=adminId, viewMode='off') *viewMode = on or off*

"""






"""
*Get the id of all users who sent a message to the chat*

uids = client.getUid(adminId=adminId)
print(uids)

"""


"""
*Change background with link*

client.edit_background(adminId=adminId, imgUrl="Url")

"""

"""
*Change background with file*

"""
