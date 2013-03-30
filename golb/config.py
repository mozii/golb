# coding=utf8

# read config from conf.toml
#
# configurations
#   name            blog's name
#   description     blog's description
#   author          blog's author's name
#   templates       the directory's name of your templates
#   others....      (note: others settings can be touched in template files \
# in this way: blog.mysetting)

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
