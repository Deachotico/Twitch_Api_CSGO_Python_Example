'''
Example parameters
    user = 'Email@gmail.com'        #the sender
    pwd = 'abcdefgh'                #App Password Gmail
    recipient = 'Email@gmail.com'   #The recipient
    subject = 'test'                #Subject of the message
    body = 'test'                   #Body of the message

'''
def send_email(user, pwd, recipient, subject, body):
    import smtplib
#SendEmail

    print("user", user, "pwd", pwd, "recipient",recipient,
     "subject",subject,"==========================================================================", body)
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
    except Exception as inst:
        print (inst)
        print ("failed to send mail")