import datetime
import pytz


def date_time_to_timestamp(time):

    est_timezone = pytz.timezone('UTC')
    time_obj = datetime.datetime.strptime(
        time, '%Y-%m-%d %H:%M').replace(tzinfo=est_timezone)
    timestamp = int(time_obj.timestamp())
    return timestamp * 1000
