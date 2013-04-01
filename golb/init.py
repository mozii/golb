from ._ import src as s
from ._ import output as o
from ._ import srcExt as se
from ._ import charset

from blog import Post

from os.path import join as j
from os import makedirs as mkdir
from os.path import exists
from os import system

helloworld = u"""
title = "Hello World!"  # this is post's title
tags = ["unTaged", ]  # ["tag1", "tag2", ...]
----

```c

int main(void)
{
    printf("Hello World!");
    return 0;
}

```

"""

conf = u"""
# config for this blog
[blog]
# blog's name
name = "Follow My Heart"
# blog's description
description = "Make difference"
# the directory of your templates(required!)
templates = "templates"
# posts count for per page,default: 12
posts_per_page = 3
# blog's author
[author]
name = "hit9"  # your github username
email = "nz2324@126.com"

# other settings ..
# other settings can be touched in template files in this way:
# keygroup.key
# i.e:
# [mysettings]
# somevar = true
# you can reach this setting in templates: mysettings.somevar
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
        j(Post.sdir, "helloworld" + se), "w"
    ).write(helloworld.encode(charset))

    print "Fetch templates from github.com.."

    system("git submodule add git://github.com/hit9/golb-templates-classic.git templates")

    print "Init complete"
