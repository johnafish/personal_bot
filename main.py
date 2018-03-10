""" A personal bot designed to simplify my browsing habits """
import webbrowser
import time
import sys
from youtube import Youtube
from constants import CHECKIN_URLS, MAIL_URLS, SCHOOL_URLS
from daemon import Daemon

class PersonalBot():
    """ Personal bot: someone to do your bidding """
    def __init__(self):
        self.urls_opened = 0
        self.youtube = Youtube()
        self.daemon = Daemon()

    def parse_cmd(self, cmd):
        """ Parses string commands and shortcuts to functions """
        commands = {"c" : self.checkin,
                    "checkin" : self.checkin,
                    "e" : sys.exit,
                    "end" : sys.exit,
                    "q" : sys.exit,
                    "quit" : sys.exit,
                    "m" : self.mail,
                    "mail" : self.mail,
                    "email" : self.mail,
                    "s" : self.school,
                    "school" : self.school,
                    "y" : self.youtube.subscribers,
                    "yt" : self.youtube.subscribers}
        commands[cmd.lower()]()

    def open_urls(self, urls):
        """ Opens a set of urls with an appropriate delay """
        for url in urls:
            self.urls_opened += 1
            webbrowser.open(url, new=2)
            time.sleep(1)

    def checkin(self):
        """ Opens earnings checkin URLs """
        self.open_urls(CHECKIN_URLS)

    def mail(self):
        """ Opens both mail accounts of mine """
        self.open_urls(MAIL_URLS)

    def school(self):
        """ Opens my school related tabs """
        self.open_urls(SCHOOL_URLS)

if __name__ == "__main__":
    BOT = PersonalBot()
    while True:
        BOT.parse_cmd(input())
