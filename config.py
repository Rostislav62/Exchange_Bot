# Telegram bot token
TOKEN = '7148692650:AAGgk9MkQJKicsPsK3GD-QhTku5u1XILIfQ'

# URL for the CryptoCompare API
CRYPTOCOMPARE_URL = 'https://min-api.cryptocompare.com/data/price'

# Message indicating data source
CRYPTOCOMPARE_MESSAGE = 'Data provided by [cryptocompare.com](https://www.cryptocompare.com/)'

# Dictionary of available currencies and their symbols
keys = {
    'bitcoin': 'BTC',
    'efirium': 'ETH',
    'dollar': 'USD',
    'euro': 'EUR',
    'rubli': 'RUB',
    'yuani': 'CNY',
    'yena': 'JPY'
}

# Start and help message
START_HELP_MESSAGE = (
    'Hello!\n'
    'I am a bot assistant in currency conversion.\n'
    '\nTo get instructions, click: /help\n'
    'To see a list of available currencies, click: /values'
)

# Help message with detailed instructions
HELP_MESSAGE = (
    'Hello!\n'
    '\nTo get the exchange rate of two currencies relative to each other you must:\n'
    'enter the name of the currency whose price you want to know (base currency),\n'
    'enter the name of the currency in which you want to know the price of the first currency '
    '(quote currency), separated by a space,\n'
    'and the amount of the first currency, separated by a space.\n'
    '\n<base currency> <quote currency> <amount of base currency> \n'
    '\nFor example:\n '
    'euro dollar 12'
    '\nTo see a list of available currencies, click: /values'
)

# Message listing available currencies
VALUES_MESSAGE = 'Available currencies:\n' + '\n'.join(keys.keys())

# Generic error message
ERROR_MESSAGE = 'User error'
