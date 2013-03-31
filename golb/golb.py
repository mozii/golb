# coding=utf8
"""
Usage:
  golb <command>
  golb (-h | --help)
  golb (-v | --version)
Options:
  -h   --help    show this
  -v --version   show version
Commands:
  init        init current directory as a golb working directory
  build       build blog

"""

from .init import init
from .build import build
from docopt import docopt


def main():
    # parse the arguments
    dct = docopt(__doc__, version='golb version 0.1')
    c = dct["<command>"]
    if c == "init":
        init()
    elif c == "build":
        build()
    else:
        exit(__doc__)

if __name__ == '__main__':
    main()
