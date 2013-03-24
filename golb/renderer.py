# coding=utf8
#
# render templates
#
import blog
from ._ import templates
from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader(templates)
env = Environment(loader=loader)

g = dict(blog=blog)

def render(dct, template):
    tpl = env.get_template(template)
    dct.update(g)
    return tpl.render(**dct)
