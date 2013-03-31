# coding=utf8
# global vars
# charset utf8 everywhere
charset = "utf8"
# source filename's extension
srcExt = ".md"
# output filename's extension
outputExt = ".html"
# separator for head and body in each source file
separator = "----"
# source directory
src = "src"
# output directory
output = "."
# templates directory
from .config import templates
# posts count of per page,  should not be shared as blog's attr
from .config import posts_per_page
