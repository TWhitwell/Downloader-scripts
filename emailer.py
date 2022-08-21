import pickle
import os
import base64
import googleapiclient.discovery
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Get the path to the pickle file
home_dir = os.path.expanduser('~')
pickle_path = os.path.join(home_dir, 'gmail.pickle')

# Load our pickled credentials
creds = pickle.load(open(pickle_path, 'rb'))

# Build the service
service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)

# Create a message
my_email = 'thomaswhitwell123@gmail.com'
msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = f'{my_email}'
msg['To'] = 'thomaswhitwell1@gmail.com'
msgPlain = plain
msgHtml = html
msg.attach(MIMEText(msgPlain, 'plain'))
msg.attach(MIMEText(msgHtml, 'html'))
raw = base64.urlsafe_b64encode(msg.as_bytes())
raw = raw.decode()
body = {'raw': raw}

message1 = body
message = (
    service.users().messages().send(
        userId="me", body=message1).execute())
print('Message Id: %s' % message['id'])