#coding=utf8

#
# write post
#
import os
from ._ import *

PostOutputDir = os.path.join(OutputDir, PostDir)


# content: unicode string
def writePost(name, content):
    fn = name + OutputNameExt
    fp = os.path.join(PostOutputDir, fn)
    # encode to utf8
    content = content.encode(CharSet)
    # write to output
    dir = os.path.dirname(fp)

    if dir and os.path.exists(dir) == False:
        # if output dir not exists, make it
        os.makedirs(dir)

    open(fp, "w").write(content)
