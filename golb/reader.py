#coding=utf8
#
# read source file,  if not found. raise exception
#

from ._ import *
from os.path import join as j

# read Post, return unicode content
def readPost(name):
    fn = name + SrcNameExt
    fp = j(SrcDir, PostDir, fn)

    try:
        content = open(fp).read()
    except:
        raise Exception(
            "Failed to read post " + name
        )

    # decode to unicode
    try:
        content = content.decode(CharSet)
    except:
        raise Exception(
            "Post " + name + " not encode " + CharSet
        )

    return content
