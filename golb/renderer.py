# coding=utf8
#
# render templates
#
from ._ import templates
from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader(templates)
env = Environment(loader=loader)
env.trim_blocks = True

def render(dct, template):
    # dct: vars to pass to templates
    return env.get_template(template).render(**dct)
