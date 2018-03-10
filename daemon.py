""" Threads to run constantly """
import time
from threading import Thread
import youtube

def youtube_thread():
    """ Print Youtube Subs Every 5 minutes """
    while True:
        youtube.subscribers()
        time.sleep(300)

def start_threads():
    """ Start list of threads """
    yt_thread = Thread(target=youtube_thread)
    yt_thread.start()
