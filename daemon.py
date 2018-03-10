""" Threads to run constantly """
import time
from threading import Thread
from youtube import Youtube

class Daemon():
    def __init__(self):
        self.start_threads()

    def youtube_thread(self):
        """ Print Youtube Subs Every 5 minutes """
        yt_instance = Youtube()
        while True:
            yt_instance.subscribers()
            time.sleep(300)

    def start_threads(self):
        """ Start list of threads """
        yt_thread = Thread(target=self.youtube_thread)
        yt_thread.start()
