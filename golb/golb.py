# coding=utf8
"""
Usage: golb <command> [-hv]
Options:
  -h   --help    show this
  -v --version   show version
Commands:
  init        init current directory as a golb working directory
  build       build blog


"""
from docopt import docopt
from .build import build

def main():
    # parse the arguments
    dct = docopt(__doc__, version='golb version 0.1')
    c = dct["<command>"]
    if c == "init":
        print "init.."
    elif c == "build":
        build()
    else:
        exit(__doc__)
