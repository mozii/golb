# coding=utf8
#
# Read conf.py and update the default settings
#

# Source files directory
src = "src"
# output directory
output = "."
# where the templates in?
templates = "templates"
# blog name
name = "Hello World"
# blog description
description = "Make difference."
# blog's author
author = "You"

# import conf.py to update the settings above

try:
    from conf import *
except ImportError:
    # if import error, do nothing
    # use the default vars
    pass
