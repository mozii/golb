#coding=utf8
#
# read source file,  if not found. raise exception
#

import post
from ._ import src
from ._ import srcExt
from ._ import charset
from os.path import join as j

# read Post, return unicode content
def readPost(name):
    fn = name + srcExt
    fp = j(src, post.dir, fn)

    try:
        content = open(fp).read()
    except:
        raise Exception(
            "Failed to read post " + name
        )

    # decode to unicode
    try:
        content = content.decode(charset)
    except:
        raise Exception(
            "Post " + name + " not encode " + charset
        )

    return content
