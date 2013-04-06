#coding=utf8
from ._ import src as s
from ._ import output as o
from ._ import srcExt as se
from ._ import outputExt as oe
from os.path import join as j
from os.path import getmtime
from datetime import datetime


class Post(object):

    src_dir = j(s, "post")  # source's dir
    out_dir = j(o, "post")  # output's dir
    template = "post.html"  # all posts are rendered with this template

    def __init__(self, filename):
        """
        filename
          post's filename with extension i.e. "I-am-a-post.md"
        """
        self.name = filename[:-len(se)]  # post's name i.e. "I-am-a-post"
        self.filename = filename
        self.src = j(Post.src_dir, self.name + se)  # source path
        self.out = j(Post.out_dir, self.name + oe)  # output path
        # post's update time
        self.update_at = datetime.fromtimestamp(getmtime(self.src))


class Tag(object):

    out_dir = j(o, "tag")
    template = "tag.html"

    def __init__(self, name, posts=list()):
        """
        name
          tag's name  i.e.  "I-am-a-tag"
        posts
          list of post taged this name
        """
        self.name = name
        self.posts = posts
        self.out = j(Tag.out_dir, name + oe)


class Page(object):

    out_dir = j(o, "page")
    template = "page.html"

    def __init__(self, number, posts=list()):
        self.number = number
        self.posts = posts
        self.out = j(Page.out_dir, str(number) + oe)
        self.first = False  # is the first page?
        self.last = False  # is the last page?


# other pages
class Other(object):

    def __init__(self, **attrs):
        # set attributes to self
        for name, value in attrs.items():
            setattr(self, name, value)


# index
index = Other(out=j(o, "index" + oe))

# archives page
archives = Other(
    out=j(o, "archives" + oe),
    template="archives.html"
)

# about.html
about = Other(
    src=j(s, "about" + se),
    out=j(o, "about" + oe),
    template="about.html"
)

# tags
tags = Other(
    out=j(o, "tags" + oe),
    template="tags.html"
)
