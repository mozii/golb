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
    l = None

    for lineno, line in enumerate(lines):
        if separator in line:
            l = lineno
            break  # use the first ----

    if not l:
        raise Exception("Separator not found.")

    hd = lines[:l]
    bd = lines[l+1:]

    head, body = "\n".join(hd), "\n".join(bd)

    # parse head
    dct = toml.loads(head)
    # add markdown, html key
    dct["markdown"] = body
    dct["html"] = markdown.render(body)
    # add summary, use the first 5 line
    su = bd[:5]
    dct["summary"] = markdown.render("\n".join(su))
    return dct
