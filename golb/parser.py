#coding=utf8
# parser for content (unicode required str)

from ._ import charset
from ._ import separator
import houdini as h
import toml_ply as toml
import misaka as m
from misaka import HtmlRenderer, SmartyPants
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


class ColorRenderer(HtmlRenderer, SmartyPants):

    def block_code(self, text, lang):

        if not lang:
            text = text.encode(charset)
            return (
                '\n<pre><code>%s</code></pre>\n' % h.escape_html(text.strip())
            )

        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()

        return highlight(text, lexer, formatter)

renderer = ColorRenderer()

markdown = m.Markdown(
    renderer,
    extensions=m.EXT_FENCED_CODE | m.EXT_NO_INTRA_EMPHASIS
)


# Parse toml+markdown str(in unicode format)
def parse(content):

    lines = content.split("\n")

    separatorLine = None

    for line in lines:
        if separator in line:
            separatorLine = line
            break

    if not separatorLine:
        raise Exception(
            "Separator not found."
        )

    head, body = tuple(content.split(separatorLine))

    # parse head
    dct = toml.loads(head)
    # add markdown, html key
    dct["markdown"] = body
    dct["html"] = markdown.render(body)
    return dct
