""" Get value of portfolio from market """
import requests
from database import Database

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

if __name__ == "__main__":
    PORTFOLIO = Portfolio()
    PORTFOLIO.write_portfolio_value()
