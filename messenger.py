import nexmo
import os

class Messenger:
	def __init__(self):
		self.client = nexmo.Client(
			key=os.environ['NEXMO_API_KEY'],
			secret=os.environ['NEXMO_API_SECRET']
		)

	def send_message(self, message, recipient):
		responseData = self.client.send_message(
		    {
		        "from": 15043754374,
		        "to": recipient,
		        "text": message,
		    }
		)

		if responseData["messages"][0]["status"] == "0":
		    return True
		else:
		    print("Message failed with error: %s " % responseData['messages'][0]['error-text'])
		    return False