#coding=utf8

# force utf8!
CharSet = "utf-8"
PostDir = "post"
PostTemplate = "post.html"
TagTemplate = "tag.html"
PageTemplate = "page.html"
SrcNameExt = ".md"

# import settings
from .config import *
from os import path

PostSrcDir = path.join(SrcDir, PostDir)
