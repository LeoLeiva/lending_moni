import logging
from datetime import datetime
from django.conf import settings
from pytz import timezone as pytz_timezone


def get_logger(name):
    """Get and return logger with given name."""
    if not name:
        raise Exception("Need to provide a name for the logger")
    return logging.getLogger(name)

def get_current_time(timezone_str=None):
    """
    Get and return the current time of a given place.

    :param timezone_str: The timezone string for the location, defaulted to
        the one of Buenos Aires, Argentina.
    :return: The datetime object with the current time for the given place.
    """
    if timezone_str is None:
        timezone_str = settings.TIME_ZONE

    tz_obj = pytz_timezone(timezone_str)
    now_time = datetime.now(tz_obj)
    return now_time
