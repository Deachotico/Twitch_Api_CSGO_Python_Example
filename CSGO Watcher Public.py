import urllib.request
import logging
import os 
import json
import email.utils
import smtplib

#Request to Twitch
try:
    url = 'https://api.twitch.tv/kraken/streams/?game=Counter-Strike%3A%20Global%20Offensive&limit=3'
    req = urllib.request.Request(url)
    req.add_header("Client-ID","PUT_YOUR_ID_HERE")
    resp = urllib.request.urlopen(req)
    data = resp.read()
except:
    quit()

#Building the json in memory
data = str(data)
data = data.replace("b'{", "{")
data = data.replace("}}'", "}}")
data = data.replace("\''", "}}")
response = json.loads(data)


#Read and Filter
email_body = ''
for streams in response['streams']:
    #Build the email body with all streams over 20000 watching
    if (streams['viewers'] > 20000):
        email_body = email_body+"Stream Name:\n"+streams['channel']['status']+'\n'
        email_body = email_body+"Channel:\n"+streams['channel']['display_name']+'\n'
        email_body = email_body+"Viewers:\n"+str(streams['viewers'])+'\n'
        email_body = email_body+"Game:\n"+streams['channel']['game']+'\n'
        #email_body = email_body+"Start Time:\n"+streams['created_at']+'\n'
        #img ="<img src='{0!s}' alt='Logo' title='Logo' style='display:block' width='200' height='87' />".format(streams['preview']['medium'])
        #img.replace('/','//[, 1]')
        #email_body = email_body+str(img)+'\n'
        email_body = email_body+"Link:\n"+streams['channel']['url']+'\n\n\n'

if (email_body!= ''):
    #SendEmail
    user = 'email@gmail.com' 
    pwd = 'APP_PASSWORD_GMAIL_HERE'
    recipient = 'email@gmail.com'
    subject = 'CSGO New Livestreams at Twitch'
    body = email_body

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")
else:
    print("No interesting streams right now")
