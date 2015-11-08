'''
Created on Nov 7, 2015

@author: catzhangy3
'''
import db2

import smtplib
from email.mime.text import MIMEText

API_USER = "easyflightdeals@gmail.com"
API_KEY = "4IQ28aKA3wuw7bd1zu3j"


# Analyzes contacts and sends emails and texts
def send_email_and_text(db, fields, new_entries):
    persons = db2.field_query(db, fields, "contact_list")
    mailing_list = dict()
    for p in persons:
        if p not in mailing_list:
            mailing_list[(p[1], p[2])] = {
                "name": p[0],
                "matches": set(),
            }
        mailing_list[(p[1], p[2])]["matches"].add("%s -> %s" % (p[3], p[4]))

    server = start_server()
    for k, v in mailing_list.items():
        send_email(k, v, server)
    quit_server(server)


def start_server():
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(API_USER, API_KEY[::-1])
    return server


def quit_server(server):
    server.quit()


# k is tuple of email and phone number
# v is name and matches
def send_email(k, v, server):
    if k[0]:
        msg = MIMEText(''.join([
            "Hi %s, \n\n" % v["name"],
            "You requested to receive notifications for new ",
            "JetBlue Getaway deals that match your desires!\n\n",
            "We are writing to let you know that there are matches ",
            "available for you! Come check out the new deals ",
            "at Easy Flight Deals!\n\n",
            "The following origin -> destination pairs matched ",
            "for you: %s" % ", ".join([str(m) for m in v["matches"]]),
            "\n\nSincerely, \n",
            "Easy Flight Deals",
        ]))
        msg['Subject'] = "[Notification] New Jetblue Getaway Deal!"
        msg['From'] = API_KEY
        msg['To'] = k[0]
        server.sendmail(API_KEY, k[0], msg.as_string())

# jk: significant other's email
# k: tuple of user email and phone number
# w: name of user and randomly selected getaway
def funtimes(jk, k, w, server):
    if jk and k[0]:
        msg = MIMEText(''.join([
            "Hi %s's significant other, \n\n" % w["name"],
            "Congratulations!  We are writing to inform you that ",
            "you and %s have been selected to win a JetBlue Free Getaway!\n\n" %w["name"],
            "You will be flying from",
            " %s.\n\n" % w["rand"],
            "For more great deals, book your next geteaway ",
            "with Easy Flight Deals!"
            "\n\nSincerely, \n",
            "Justin Bieber",
        ]))
        msg['Subject'] = "[Notification] New Jetblue Getaway Giveaway!"
        msg['From'] = API_KEY
        msg['To'] = jk
        server.sendmail(API_KEY, jk, msg.as_string())

        msg = MIMEText(''.join([
            "Hi %s, \n\n" % w["name"],
            "Great news!  You and your significant other will be ",
            "on a getaway from %s!\n\n" % w["rand"],
            "Unfortunately, you will have to pay for this trip. \n\n",
            "Don't let your significant other down! ",
            "Head to Easy Flight Deals to finish the booking ",
            "and check out other great getaway deals!\n\n",
            "\n\nSincerely, \n",
            "Easy Flight Deals\n\n",
            "Powered by JetBlue."
        ]))
        msg['Subject'] = "[Notification] New Jetblue Getaway Deal!"
        msg['From'] = API_KEY
        msg['To'] = k[0]
        server.sendmail(API_KEY, k[0], msg.as_string())


v = {"name": "Catherine", "matches": set()}
v["matches"].add("ABC -> DEF")
v["matches"].add("GFH -> IJK")
k = ("catzhangy1@gmail.com", 0)

k = ("jackson.chang@berkeley.edu", 0)
w = {"name": "Jackson", "rand": "ORD -> CUN"}
jk = "kai.si@berkeley.edu"
s = start_server()
send_email(k, v, s)
funtimes(jk, k, w, s)
quit_server(s)