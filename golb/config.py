# coding=utf8
#
# Read conf.py and update the default settings
#

# separator for head and body(or say markdown) in your source file
# why not use the default
Separator = "----"
# Source files directory
SrcDir = "src"
# output directory
OutputDir = "."
# where the templates in?
TemplatesDir = "templates"

# import conf.py to update the settings above

try:
    from conf import *
except ImportError:
    # if import error, do nothing
    # use the default vars
    pass
