""" Get value of portfolio from market """
from datetime import date
import requests
from database import Database
import helpers

class Portfolio():
    """ A portfolio of traded securities """
    def __init__(self):
        self.key = open("secrets/alphavantage.txt", "r").readline()
        self.database = Database()

    def create_table(self):
        """ Initialize Portfolio table in database """
        columns = [{"name": "ticker", "type": "text"},
                   {"name": "price", "type": "real"},
                   {"name": "quantity", "type": "int"}]
        self.database.create_table("portfolio", columns)

    def create_value_table(self):
        """ Initialize value table """
        columns = [{"name": "value", "type": "real"},
                   {"name": "date", "type": "datetime default current_timestamp"}]
        self.database.create_table("portfolio_value", columns)

    def new_position(self, ticker, price, quantity):
        """ Insert a position into the database """
        self.database.cursor\
                .execute("INSERT INTO portfolio (ticker, price, quantity) VALUES ('{0}', {1}, {2})"\
                .format(ticker, price, quantity))
        self.database.connection.commit()

    def get_positions(self):
        """ Return a list of all positions in database """
        return self.database.cursor.execute("SELECT * from portfolio").fetchall()

    def current_price(self, symbol):
        """ Get current price of stock from alphavantage """
        request_url = "https://www.alphavantage.co/query?"\
                      "function=TIME_SERIES_INTRADAY&symbol={0}&interval=1min&apikey={1}"\
                      .format(symbol, self.key)
        request = requests.get(request_url)
        if request.status_code != 200:
            return False

        for _key, value in request.json()["Time Series (1min)"].items():
            return float(value["4. close"])

    def portfolio_value(self):
        """ Get overall value of portfolio """
        value = 0
        for position in self.get_positions():
            value += self.current_price(position[0]) * position[2]
        return value

    def initial_value(self):
        """ Get initial value of portfolio """
        value = 0
        for position in self.get_positions():
            value += position[1] * position[2]
        return value

    def portfolio_pnl(self):
        """ Get overall profit/loss of portfolio """
        return self.portfolio_value() - self.initial_value()

    def write_portfolio_value(self):
        """ Write portfolio value to database """
        self.database.cursor.execute("INSERT INTO portfolio_value (value) VALUES({0})"\
                                     .format(self.portfolio_value()))
        self.database.connection.commit()

    def daily_data(self):
        """ Gets rows entered since start of day """
        return self.database.cursor\
                            .execute("SELECT * from portfolio_value WHERE date >= '{0}'"\
                            .format(date.today())).fetchall()

    def daily_pnl(self):
        """ Gets difference in value since start of day """
        daily_data = self.daily_data()
        first = daily_data[0]
        last = daily_data[-1]
        return last[0] - first[0]

    def daily_percentile_pnl(self):
        """ Returns daily pnl as percentage """
        starting_value = self.daily_data()[0][0]
        return self.daily_pnl() / starting_value

    def value(self):
        """ Gets value, writes to db, prints daily pnl """
        self.write_portfolio_value()
        current_pnl = self.daily_pnl()
        percentile_pnl = self.daily_percentile_pnl()
        print("Portfolio")
        print("{0} ({1})".format(helpers.pretty_num_to_s(current_pnl, money=True), helpers.pretty_num_to_s(percentile_pnl, percentage = True)))

if __name__ == "__main__":
    PORTFOLIO = Portfolio()
    PORTFOLIO.value()
