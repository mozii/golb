from ._ import src as s
from ._ import output as o
from ._ import srcExt as se
from ._ import charset

from blog import Post

from os.path import join as j
from os import makedirs as mkdir
from os.path import exists

helloworld = u"""
title = "helloworld"  # this is post's title
tags = ["unTaged", ]  # ["tag1", "tag2", ...]
----
## Hello World!
"""

conf = u"""
# config for this blog

# blog's name
name = "HelloWorld"
# blog's description
description = "Make difference"
# blog's author
author = "yourname"
# the directory of your templates(required!)
templates = "templates"
# other settings ..
# other settings can be touched in template files in this way: blog.mysetting
"""


def init():

    if not exists(".git"):
        exit("Please init here a git repo first.")

    print "mkdir " + Post.sdir + ".."
    mkdir(Post.sdir)
    # write conf.toml
    print "write default config to conf.toml.."
    open("conf.toml", "w").write(conf.encode(charset))
    # write sample posts
    print "write you a sample post.."
    open(
        j(Post.sdir, "helloworld" + se),"w"
    ).write(helloworld.encode(charset))

    print "Init complete"
