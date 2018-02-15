import webbrowser

checkin_urls = ["https://www.youtube.com/dashboard?o=U", "https://my.questrade.com/trading/account/balances", "https://affiliate-program.amazon.com/home"]

def checkin():
    for url in checkin_urls:
        webbrowser.open(url, new = 2)

checkin()
