import smtplib
import email.utils
gmail_user = 'testajit8gmail.com'
gmail_app_password = 'Testajit8#123'
sent_from = gmail_user
sent_to = ['prashant.dey@herovired.com', 'ajit_aitm@yahoo.com']
sent_subject = 'Notification Recieved from Ajit Singh'
sent_body = 'Hi Prashant \n this is trigger email from lambda fumction when Uploading any image on S3'
email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)
try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text.encode("utf-8"))
        server.close()
        print(email_text)
        print('Email sent!')
except Exception as exception:
        print("Error: %s!\n\n" % exception)


