import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os
import multiprocessing

bind = 'config your own'     #TODO
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = 'debug'
accesslog = "-"
errorlog = "config your own" #TODO
