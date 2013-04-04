# coding=utf8
# blog instance
from ._ import src as s
from ._ import output as o
from ._ import srcExt as se
from ._ import outputExt as oe
from .conf import conf
from os.path import join as j
from os.path import getmtime
from datetime import datetime


sel = len(se)


class Post(object):
    #
    #  minimal attributes
    #   name                i.e. "helloworld"
    #   filename            filename  i.e. "helloworld.md"
    #   srcp                source file path   "src/post/helloworld.md
    #   outp                output file path   "./post/helloworld.html"
    #   update_at           datetime object
    #   title               post's title
    #   tags                list

    sdir = j(s, "post")  # source dir
    odir = j(o, "post")  # output dir
    tpl = "post.html"

    def __init__(self, fn):  # init one Post object by filename
        name = fn[:-sel]
        self.name = name
        self.filename = fn
        self.srcp = j(Post.sdir, name + se)  # source path
        self.outp = j(Post.odir, name + oe)  # output path
        self.update_at = datetime.fromtimestamp(getmtime(self.srcp))


class Tag(object):

    odir = j(o, "tag")
    tpl = "tag.html"

    def __init__(self, name, posts=list()):
        self.name = name
        self.posts = posts
        self.outp = j(Tag.odir, name + oe)


class Page(object):

    odir = j(o, "page")
    tpl = "page.html"

    def __init__(self, number, posts=list()):
        self.number = number
        self.posts = posts
        self.outp = j(Page.odir, str(number) + oe)
        self.first = False
        self.last = False


# other pages
class Other(object):

    def __init__(self, **attrs):
        for k, v in attrs.items():
            setattr(self, k, v)

# index page
index = Other(outp=j(o, "index" + oe))

# archives page

archives = Other(
    outp=j(o, "archives" + oe),
    tpl="archives.html"
)


about = Other(
    srcp=j(s, "about" + se),
    outp=j(o, "about" + oe),
    tpl="about.html"
)

tags = Other(
    outp=j(o, "tags" + oe),
    tpl="tags.html"
)
