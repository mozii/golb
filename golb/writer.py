#coding=utf8

#
# write post
#
import post
from ._ import output
from ._ import outputExt
from ._ import charset
from os.path import join as j
from os.path import dirname, exists
from os import makedirs as mkdir

# content: unicode string
def writePost(name, content):
    fn = name + outputExt
    fp = j(output, post.dir, fn)
    # encode to utf8
    content = content.encode(charset)
    # write to output
    dir = dirname(fp)

    if dir and exists(dir) == False:
        # if output dir not exists, make it
        mkdir(dir)

    open(fp, "w").write(content)
