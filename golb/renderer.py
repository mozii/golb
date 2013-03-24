#coding=utf8
#
# render templates
#

from ._ import TemplatesDir

from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader(TemplatesDir)
env = Environment(loader=loader)

def render(g, template):
    tpl = env.get_template(template)
    return tpl.render(g=g)
