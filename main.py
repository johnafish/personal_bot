""" A personal bot designed to simplify my browsing habits """
import webbrowser
import time
import sys

CHECKIN_URLS = ["https://www.youtube.com/dashboard?o=U",
                "https://my.questrade.com/trading/account/balances",
                "https://affiliate-program.amazon.com/home",
                "https://admin.mailchimp.com"]

MAIL_URLS = ["https://mail.google.com/mail/u/" + str(i) for i in range(2)]

SCHOOL_URLS = ["https://canvas.harvard.edu",
               "https://calendar.google.com/calendar/r"]

def parse_cmd(cmd):
    """ Parses string commands and shortcuts to functions """
    commands = {"c" : checkin,
                "checkin" : checkin,
                "e" : sys.exit,
                "end" : sys.exit,
                "q" : sys.exit,
                "quit" : sys.exit,
                "m" : mail,
                "mail" : mail,
                "email" : mail,
                "s" : school,
                "school" : school}
    commands[cmd.lower()]()

def open_urls(urls):
    """ Opens a set of urls with an appropriate delay """
    for url in urls:
        webbrowser.open(url, new=2)
        time.sleep(1)

def checkin():
    """ Opens earnings checkin URLs """
    open_urls(CHECKIN_URLS)

def mail():
    """ Opens both mail accounts of mine """
    open_urls(MAIL_URLS)

def school():
    """ Opens my school related tabs """
    open_urls(SCHOOL_URLS)

if __name__ == "__main__":
    while True:
        parse_cmd(input())
