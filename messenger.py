import os
import subprocess

class Messenger:
	def __init__(self):
		self.api_key = os.environ['NEXMO_API_KEY']
		self.api_secret = os.environ['NEXMO_API_SECRET']

	def send_message(self, message, recipient):
		try:
			command = str.split("curl -X POST https://rest.nexmo.com/sms/json -d api_key=" + \
				self.api_key + " -d api_secret=" + self.api_secret + " -d")
			command = command + ["to=" + str(recipient), "-d", "from=15043754374", "-d", "text=" + message]
			output = subprocess.check_output(command)
		except subprocess.CalledProcessError as e:
			print("subprocess says that didn't work. " + str(e.cmd))
		except Exception as e:
			print("general exception. " + str(e))

		"""		
		if responseData["messages"][0]["status"] == "0":
			print(str(recipient) + " (message success)")
			return True
		else:
		    print(str(recipient) + "Message failed with error: %s " % responseData['messages'][0]['error-text'])
		    return False
		"""

	def verify(self, recipient):
		response = self.client.start_verification(number=recipient, brand="Zana")

		if response["status"] == "0":
		    print("Started verification request_id is %s" % (response["request_id"]))
		else:
		    print("Error: %s" % response["error_text"])