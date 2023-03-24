'''
rise error
'''

import sys


def errors(exchange_name, response):
    if exchange_name == 'bybit':
        response = response.json()['retCode']
    if exchange_name == 'bybit':
        if response == 10001:
            sys.exit(
                ("\n Error Code 10001: Request parameter error. Invalid symbol."))

        if response == 10006:
            sys.exit(
                ("\n Error Code 10006: Too many visits. Exceeded the API Rate Limit.."))

        if response == 10001:
            sys.exit(
                ("\n Error Code 10009: IP has been banned."))
    if exchange_name == 'binance':
        if 'code' in response.json():

            response = response.json()['code']
            if response == -1121:

                sys.exit(
                    ("\n Error Code -1121: Request parameter error. Invalid symbol."))

            if response == -1003 or -1121:
                sys.exit(
                    ("\n Error Code -1003: Too many visits. Exceeded the API Rate Limit.."))
            if response == -1021:
                sys.exit('INVALID_TIMESTAMP')
