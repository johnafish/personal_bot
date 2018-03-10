""" Simple Youtube Analytics """
import requests
from database import Database

class Youtube():
    def __init__(self):
        data_file = open("secrets/youtube.txt", "r")
        self.channel_id = data_file.readline()
        self.key = data_file.readline()
        self.db = Database()

    def create_table(self):
        columns = [{"name": "subscribers", "type": "int"},
                   {"name": "date", "type": "datetime default current_timestamp"}]
        self.db.create_table("youtube", columns)

    def subscribers(self):
        subscribers = self.get_subscribers()
        self.write_subscribers_to_db(subscribers)
        daily_subscriptions = self.daily_subscribers()
        daily_sub_string = ""
        if daily_subscriptions > 0:
            daily_sub_string += '\033[92m'
            daily_sub_string += "+{0}".format(daily_subscriptions)
        else:
            daily_sub_string += '\033[91m'
            daily_sub_string += "{0}".format(daily_subscriptions)
        daily_sub_string += '\033[0m'

        print("{0} ({1})".format(subscribers, daily_sub_string))

    def get_subscribers(self):
        """ Print the number of subscribers to channel """
        payload = {"part": "statistics",
                   "channel": self.channel_id, 
                   "key": self.key, 
                   "forUsername": "MrFish235"}
        url = "https://www.googleapis.com/youtube/v3/channels"
        request = requests.get(url, params=payload)
        return request.json()["items"][0]["statistics"]["subscriberCount"]

    def write_subscribers_to_db(self, subscribers):
        """ Write the number of subscribers to the database """
        self.db.cursor.execute("INSERT INTO youtube (subscribers) VALUES({0})".format(subscribers))
        self.db.connection.commit()

    def daily_subscribers(self):
        daily_data = self.db.cursor.execute("SELECT * from youtube WHERE date >= '2018-03-10'").fetchall()
        first = daily_data[0]
        last = daily_data[-1]
        return (last[0] - first[0])

if __name__ == "__main__":
    youtube = Youtube()
    youtube.subscribers()
