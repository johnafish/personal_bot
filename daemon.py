""" Threads to run constantly """
import time
from threading import Thread
from youtube import Youtube
from stocks import Portfolio

def daily_thread():
    """ Print daily data every minute """
    youtube = Youtube()
    portfolio = Portfolio()
    while True:
        try:
            youtube.subscribers()
            portfolio.value()
        except ConnectionError:
            time.sleep(300)
        time.sleep(60)

def youtube_thread():
    """ Print Youtube Subs Every minute """
    yt_instance = Youtube()
    while True:
        try:
            yt_instance.subscribers()
        except ConnectionError:
            time.sleep(300) # Sleep if error
        time.sleep(60)


class Daemon():
    """ Run an arbitrary number of threads in the background of the bot """
    def __init__(self):
        self.threadlist = [daily_thread]
        self.active_threads = []
        self.start_threads()

    def start_threads(self):
        """ Start list of threads """
        for thread in self.threadlist:
            active_thread = Thread(target=thread)
            active_thread.start()
            self.active_threads.append(active_thread)

    def end_threads(self):
        """ End all active threads """
        for thread in self.active_threads:
            thread.exit()
