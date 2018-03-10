""" A personal bot designed to simplify my browsing habits """
import webbrowser
import time
import sys
import youtube
from constants import CHECKIN_URLS, MAIL_URLS, SCHOOL_URLS

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
                "school" : school,
                "y" : youtube.subscribers,
                "yt" : youtube.subscribers}
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
