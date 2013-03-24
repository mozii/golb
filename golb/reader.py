#coding=utf8
#
# read source file,  if not found. raise exception
#

import os
from ._ import *

PostSrcDir = os.path.join(SrcDir, PostDir)

# read Post, return unicode content
def readPost(name):
    fn = name + SrcNameExt
    fp = os.path.join(PostSrcDir, fn)

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
