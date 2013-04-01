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
  clean       rm output files
"""

from .init import init
from .build import build
from .clean import clean
from docopt import docopt


def main():
    # parse the arguments
    dct = docopt(__doc__, version='golb version 0.1')
    c = dct["<command>"]
    if c == "init":
        init()
    elif c == "build":
        build()
    elif c == "clean":
        clean()
    else:
        exit(__doc__)

if __name__ == '__main__':
    main()
