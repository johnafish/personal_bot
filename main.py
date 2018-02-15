import webbrowser, time, sys

checkin_urls = ["https://www.youtube.com/dashboard?o=U", "https://my.questrade.com/trading/account/balances", "https://affiliate-program.amazon.com/home"]

def parse_cmd(cmd):
    commands = {
            "c" : checkin,
            "checkin" : checkin,
            "e" : sys.exit,
            "end" : sys.exit,
            "q" : sys.exit,
            "quit" : sys.exit,
            "m" : mail,
            "mail" : mail,
            "email" : mail }
    commands[cmd.lower()]()

def checkin():
    for url in checkin_urls:
        webbrowser.open(url, new = 2)
        time.sleep(1)

def mail():
    for i in range(2):
        webbrowser.open("https://mail.google.com/mail/u/" + str(i), new = 2)
        time.sleep(1)

if __name__ == "__main__":
    while True:
        parse_cmd(input())
