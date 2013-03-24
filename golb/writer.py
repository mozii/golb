#coding=utf8

#
# write post
#

from ._ import *
from os.path import join as j
from os.path import dirname, exists
from os import makedirs as mkdir

# content: unicode string
def writePost(name, content):
    fn = name + OutputNameExt
    fp = j(OutputDir, PostDir, fn)
    # encode to utf8
    content = content.encode(CharSet)
    # write to output
    dir = dirname(fp)

    if dir and exists(dir) == False:
        # if output dir not exists, make it
        mkdir(dir)

    open(fp, "w").write(content)
