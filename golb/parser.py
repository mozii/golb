# coding=utf8
# parser for source file

import toml
import misaka as m
import houdini as h
from ._ import charset
from ._ import separator
from pygments import highlight
from misaka import HtmlRenderer, SmartyPants
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


class ColorRenderer(HtmlRenderer, SmartyPants):

    def block_code(self, text, lang):

        if not lang:
            text = text.encode(charset)
            return (
                '\n<div class="highlight"><pre><code>%s</code></pre></div>\n' % h.escape_html(text.strip())
            )

        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()

        return highlight(text, lexer, formatter)

renderer = ColorRenderer()

markdown = m.Markdown(
    renderer,
    extensions=m.EXT_FENCED_CODE | m.EXT_NO_INTRA_EMPHASIS
)


# method: parse
# input: unicode string( head: toml, body: markdown )
# output: dict(markdown, html, toml-dict..)
def parse(content):
    lines = content.splitlines()
    separatorLine = None

    for line in lines:
        if separator in line:
            separatorLine = line
            break

    if not separatorLine:
        raise Exception("Separator not found.")

    head, body = tuple(content.split(separatorLine))

    # parse head
    dct = toml.loads(head)
    # add markdown, html key
    dct["markdown"] = body
    dct["html"] = markdown.render(body)
    return dct
