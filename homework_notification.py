from trycourier import Courier

def send_homework_notification(name, course, email, due_date, phone_number, meet_link):
	client = Courier(auth_token="YOUR AUTHENTICATION TOKEN HERE")

	resp = client.send(
  	event = "YOUR EVENT ID HERE",
	recipient = "YOUR RECIPIENT ID HERE",
	profile = {
		"email": email,
		"phone_number": phone_number
	},
	data={
		"name": name,
		"class": course,
		"due_date": due_date,
		"meeting_link": meet_link
	},
	)

	print(resp['messageId'])
# Note the variables above were particular to the notifications I created in the Courier designer
# You *must* create a Courier account and manage integrations in order to create/use notifications