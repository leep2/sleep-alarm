import os
import configparser
import fitbit
from datetime import datetime
import json
import smtplib

CONFIG_FOLDER = 'sleep-alarm'

def email_alert():

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(config['DEFAULT']['from_email'], config['DEFAULT']['p'])

    # message to be sent
    message = 'Wake up'

    # sending the mail
    s.sendmail(config['DEFAULT']['from_email'], config['DEFAULT']['to_email'], message)

    # terminating the session
    s.quit()

os.chdir(os.path.join(os.getcwd(), CONFIG_FOLDER))
config = configparser.ConfigParser()
config.read('config.ini')

client = fitbit.Fitbit(
    config['DEFAULT']['client'],
    config['DEFAULT']['sec'],
    access_token=config['DEFAULT']['access'],
    refresh_token=config['DEFAULT']['refresh']
)

data = client.get_sleep(datetime.now())

#Logs current sleep
with open(datetime.now().strftime('%H%M') + '.json', 'w') as outfile:
    json.dump(data, outfile)

if data['summary']['totalMinutesAsleep'] >= int(config['DEFAULT']['sleeptime']):
    email_alert()