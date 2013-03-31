# coding=utf8

import toml
from ._ import charset
from os.path import exists

conffn = "conf.toml"

# minimal & default configuration
conf = dict(
    name=u"HelloWorld!",
    description=u"Make difference",
    author=u"you!",
    templates="templates",
    posts_per_page = 12
)


if exists(conffn):
    dct = toml.loads(open(conffn).read().decode(charset))
    conf.update(dct)


templates = conf.pop("templates")
posts_per_page = conf.pop("posts_per_page")
blogConf = conf
