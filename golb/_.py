# coding=utf8
# global vars for golb
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
# config filename
conf_fn = "conf.toml"
# the default & minimal settings
default_conf = dict(
    blog=dict(
        name=u"Hello World",
        description=u"Make difference",
        templates="templates",
        url="http://example.com",
    ),
    author=dict(
        name=u"your-github-username",
        email=u"you@some.com"
    )
)
