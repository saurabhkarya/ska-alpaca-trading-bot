import alpaca_trade_api as tradeapi

alpaca_endpoint = 'https://paper-api.alpaca.markets'

alpaca = tradeapi.REST(api_key,
                       api_secret, alpaca_endpoint)

order = alpaca.submit_order(
    symbol='BTCUSD',
    qty=1,
    type='limit',
    side='buy',
    limit_price=57000,
    time_in_force='day')

account = alpaca.get_account()
print(account.status)


class Martingale(object):
    def __init__(self):
        self.key = api_key
        self.secret = api_secret
        self.alpaca_endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(self.key, self.secret, self.alpaca_endpoint)
        self.symbol = 'BTCUSD'
        self.current_order = None
        self.last_price = 1

        try:
            self.position = int(self.api.get_position(self.symbol).qty)
        except:
            self.position = 0

    def submit_order(self, target):
        if self.current_order is not None:
            self.api.cancel_order(self.current_order.id)

        delta = target - self.position
        print(delta, target, self.position)
        if delta == 0:
            return
        print("Processing the order for {} shares".format(target))

        if delta > 0:
            buy_quantity = delta
            if self.position < 0:
                buy_quantity = min(abs(self.position), buy_quantity)
                print('Buying {} shares'.format(buy_quantity))
                self.current_order = self.api.submit_order(
                    self.symbol, buy_quantity, 'buy', 'limit', 'day', self.last_price)

        elif delta < 0:
            sell_quantity = abs(delta)
            if self.position > 0:
                sell_quantity = min(abs(self.position), sell_quantity)
                print('Selling {} shares'.format(sell_quantity))
                self.current_order = self.api.submit_order(
                    self.symbol, sell_quantity, 'sell', 'limit', 'day', self.last_price)


if __name__ == '__main__':
    t = Martingale()
    t.submit_order(1)
