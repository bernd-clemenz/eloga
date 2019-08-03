#
# -*- coding: utf-8-*-
# (c) 2018 ISC Clemenz & Weinbrecht GmbH
#

import argparse
from eloga import ErrorLogAnalzyer


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Simple error-log analyzer.")
    arg_parser.add_argument('--conf', type=str, default='eloga.ini')
    arg_parser.add_argument('--elogfile', type=str, default=None)
    args = arg_parser.parse_args()

    analyzer = ErrorLogAnalzyer(args.elogfile,args.conf)