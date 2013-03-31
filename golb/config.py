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
    templates="templates"
)


if exists(conffn):
    dct = toml.loads(open(conffn).read().decode(charset))
    conf.update(dct)


templates = conf.pop("templates")
blogConf = conf
