# Standard modules
from logging.handlers import TimedRotatingFileHandler
import logging
import sys


class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = \
            super(OneLineExceptionFormatter, self)\
                .formatException(exc_info)
        return repr(result)

    def format(self, record):
        s = super(OneLineExceptionFormatter, self).format(record)
        if record.exc_text:
            s = s.replace('\n', ' ')
        return s


FORMATTER = \
    OneLineExceptionFormatter(
        "[%(levelname)s] "
        "%(name)s:%(funcName)s:%(lineno)d - %(message)s")


def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(FORMATTER)
   return console_handler

def get_logger(logger_name):
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG)
   logger.addHandler(get_console_handler())
   logger.propagate = False
   return logger
