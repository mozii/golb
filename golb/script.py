# coding=utf8
"""
Usage:
  golb [--local]
  golb (-h | --help)
  golb (-v | --version)

Options:
  -h --help      show this message
  -v --version   show version
  -l --local     generate html with an empty blog url.

"""

from docopt import docopt
from .golb import build

def main():
    # parse the arguments
    dct = docopt(__doc__, version='golb version 0.1.3')
    build(local=dct["--local"])
