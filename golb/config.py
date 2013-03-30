# coding=utf8
#
# Configuration for golb
#

# default settings
#
# which set is your templates?
templates = "templates"
# blog's name
name = "Hello World"
# blog's description
description = "Make difference"
# blog's author
author = "yourname"


# try to import settings from conf.py
try:
    from conf import *
except ImportError:
    # if conf.py not found in working directory
    # then do nothing
    pass
