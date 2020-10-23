"""
def send_simple_message():
	return requests.post(
		"https://",
		auth=("api", ""), #zerobounce
		data={"from": "malliksiddharth@gmail.com",
			"to": ["siddharthmallik404@gmail.com", "malliksiddharth@gmail.com"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})




import smtplib

from email.mime.text import MIMEText

msg = MIMEText('Testing some Mailgun awesomness')
msg['Subject'] = "Hello"
msg['From']    = ""
msg['To']      = "siddharthmallik404@gmail.com"

s = smtplib.SMTP('smtp.mailgun.org', 587)

s.login('', 'password')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()




def sum(num):
	if len(num) == 1:
		return num[0]
	else:
		return num[0] + sum(num[2:])
		print(sum([2, 4, 5, 6, 7]))


word = 'aeioubcdfg'

print (word[:3] + word [3:])




import requests
from requests.exceptions import HTTPError

for url in ['https://api.facebook.com', 'https://api.jhgjhgfgdd.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')


#Max Retries
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

github_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

# Use `github_adapter` for all requests to endpoints that start with this URL
session.mount('https://api.github.com', github_adapter)

try:
    session.get('https://api.github.com')
except ConnectionError as ce:
    print(ce)




import requests
import json
import time
import sys

if len(sys.argv)>1:
	messageID = sys.argv[1]
else:
	messageID = ''
	

token = ''    # Your Postmark API token goes here
headers = {'user-agent': 'my-app/1.0', 'Accept': 'application/json', 'Content-Type': 'application/json','X-Postmark-Server-Token': '%s' % token}

r = requests.get('https://api.postmarkapp.com/messages/outbound/%s/details' % messageID, headers=headers)

response = json.loads(r.text)

status = response['Status']
if status == 'Sent':
	for event in response['MessageEvents']:
		print(event['Type'])     # 'Delivered', 'Bounced'
		print(event['ReceivedAt'])
else:
	print('Status = %s' % status)




import requests
import json

token = ''   # Your Postmark API token goes here
headers = {'user-agent': 'my-app/1.0', 'Accept': 'application/json', 'Content-Type': 'application/json','X-Postmark-Server-Token': '%s' % token}
# Make sure to add your registered 'From' address here:
data = json.dumps({'From': 'jadapa2896@onwmail.com', 'To': 'siddharthmallik404@gmail.com', 'Subject': 'Poem', 'HtmlBody': '<b>The boy stood on the burning deck</b>'})

r = requests.post('https://api.postmarkapp.com/email', headers=headers, data=data )

response = json.loads(r.text)
if response['ErrorCode'] == 0:
	print('Message ID = %s' % response['MessageID'])
else:
	print('Message not sent')
"""