""" Simple Youtube Analytics """
import requests

def subscribers():
    """ Print the number of subscribers to channel """
    data_file = open("secrets/youtube.txt", "r")
    channel_id = data_file.readline()
    key = data_file.readline()

    payload = {"part": "statistics", "channel": channel_id, "key": key, "forUsername": "MrFish235"}
    url = "https://www.googleapis.com/youtube/v3/channels"
    request = requests.get(url, params=payload)
    print(request.json()["items"][0]["statistics"]["subscriberCount"])

if __name__ == "__main__":
    subscribers()
