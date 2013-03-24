#coding=utf8

from .g import g
from ._ import PostSrcDir
from ._ import SrcNameExt
from ._ import CharSet
from ._ import PostTemplate

import os
import parser
import renderer

class Post(g):

    def __init__(self, name):
        self.name = name

    # parse this post'content and update its attr
    def parse(self):
        # read file
        filename = self.name + SrcNameExt
        filepath = os.path.join(PostSrcDir, filename)
        content = open(filepath).read()
        # decode to unicode
        try:
            content = content.decode(CharSet)
        except:
            raise Exception(
                "Post " + filepath + " not encode " + CharSet
            )

        dct = parser.parse(content)
        # update post's attributes
        self.__dict__.update(dct)

    # render post with templates/post.html
    def render(self):
        return renderer.render(self, PostTemplate)
