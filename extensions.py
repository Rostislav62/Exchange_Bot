import requests
import json
from config import keys, CRYPTOCOMPARE_URL, CRYPTOCOMPARE_MESSAGE, ERROR_MESSAGE


# Custom exception class handling API-related errors.
class APIException(Exception):
    pass


# A class to handle currency conversion using CryptoCompare API.
class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        # Gets the conversion price of the specified amount from quote currency to base currency.
        if quote == base:
            raise APIException(f'Unable to transfer identical currencies {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'We were unable to process {quote} currency.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'We were unable to process {base} currency.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'We were unable to process the quantity {amount}.')

        response = requests.get(f'{CRYPTOCOMPARE_URL}?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(response.content)[keys[base]]

        return total_base


# Handles the currency conversion process and sends the result back to the user.
def convert(bot, message):
    try:
        quote, base, amount = message.text.split()
        total_base = CryptoConverter.get_price(quote, base, amount)
        text = f'Price of {amount} {quote} in {base} = {total_base * float(amount)}\n\n{CRYPTOCOMPARE_MESSAGE}'
    except APIException as e:
        bot.reply_to(message, f'{ERROR_MESSAGE}\n{e}\n\n{CRYPTOCOMPARE_MESSAGE}')
    except Exception as e:
        bot.reply_to(message, f'Failed to process command (server error)\n{e}\n\n{CRYPTOCOMPARE_MESSAGE}')
    else:
        bot.send_message(message.chat.id, text)
