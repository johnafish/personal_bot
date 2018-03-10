""" Threads to run constantly """
import time
from threading import Thread
from youtube import Youtube

def youtube_thread():
    """ Print Youtube Subs Every 5 minutes """
    yt_instance = Youtube()
    while True:
        yt_instance.subscribers()
        time.sleep(300)


class Daemon():
    """ Run an arbitrary number of threads in the background of the bot """
    def __init__(self):
        self.threadlist = [youtube_thread]
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
