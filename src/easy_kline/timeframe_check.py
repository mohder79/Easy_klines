"""
This function checks timeframe argument is a valid timeframe or not.
A valid timeframe must be one of the in list
If the timeframe argument is not in the list of valid timeframes, function will raise an error
"""

import sys


def timeframe_check(timeframe):
    time_frames_list = ['1m', '3m', '5m',
                        '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h' , '1d', '1w']
    if timeframe not in time_frames_list:
        sys.exit(
            (f' Wrong timeframe! Timeframe must be one of: {time_frames_list}'))
