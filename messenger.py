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
			print(str(recipient) + " (message success)")
			return True
		else:
		    print("Message failed with error: %s " % responseData['messages'][0]['error-text'])
		    return False

	def verify(self, recipient):
		response = self.client.start_verification(number=recipient, brand="Zana")

		if response["status"] == "0":
		    print("Started verification request_id is %s" % (response["request_id"]))
		else:
		    print("Error: %s" % response["error_text"])