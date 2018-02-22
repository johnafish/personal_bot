""" A personal bot designed to simplify my browsing habits """
import webbrowser
import time
import sys

CHECKIN_URLS = ["https://www.youtube.com/dashboard?o=U",
                "https://my.questrade.com/trading/account/balances",
                "https://affiliate-program.amazon.com/home",
                "https://admin.mailchimp.com"]

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
                "email" : mail}
    commands[cmd.lower()]()

def checkin():
    """ Opens earnings checkin URLs """
    for url in CHECKIN_URLS:
        webbrowser.open(url, new=2)
        time.sleep(1)

def mail():
    """ Opens both mail accounts of mine """
    for i in range(2):
        webbrowser.open("https://mail.google.com/mail/u/" + str(i), new=2)
        time.sleep(1)

if __name__ == "__main__":
    while True:
        parse_cmd(input())
