#
# -*- coding: utf-8-*-
# (c) 2018 ISC Clemenz & Weinbrecht GmbH
#

import configparser
import logging
import logging.handlers

name = 'eloga'


class ErrorLogAnalyzer
    """
    A simple error log analzer based on regular expressions.
    """
    _data_file = None
    _cfg = None
    _log = None

    def __init__(data_file, config_file):
        """
        Constructor
        :param data_file: the log file to analyze
        :param config_file: the config file in INI-Format
        """
        # 1. set up configuration
        self._data_file = data_file
        self._cfg = configparser.ConfigParser()
        self._cfg.read(config_file)
        # 2. set up logging.
        self._log = logging.getLogger('eloga')
        self._log.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        rh = logging.handlers.RotatingFileHandler('eloga.log',
                                                  maxBytes=1024 * 1024,
                                                  backupCount=50)
        ch = logging.StreamHandler()
        rh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self._log.addHandler(rh)
        self._log.addHandler(ch)

    def analyze():
        self._log.info("Analyzing...")
