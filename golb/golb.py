# coding=utf8
"""
Usage:
  golb init
  golb build [--local]
  golb clean
  golb (-h | --help)
  golb (-v | --version)

Options:
  -h --help      show this message
  -v --version   show version
  -l --local     use blog.url = "", for previewing in a local server

Commands reference:
  init        init current directory as a golb working directory
  build       build blog. use -l option to build without a site's url
  clean       rm all output files
"""

from .init import init
from .build import build
from .clean import clean
from docopt import docopt


def main():
    # parse the arguments
    dct = docopt(__doc__, version='golb version 0.1')
    if dct["init"]:
        init()
    elif dct["build"]:
        build(local=dct["--local"])
    elif dct["clean"]:
        clean()

if __name__ == '__main__':
    main()
