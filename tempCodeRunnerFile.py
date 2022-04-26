import alpaca_trade_api as tradeapi

alpaca_endpoint = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(api_key,
                    api_secret, alpaca_endpoint)

account = api.get_account()
print(account.status)

order = api.submit_order(
    symbol='BTCUSD',
    qty=1,
    type='market',
    side='buy')
