#
# parser for source file
#

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
            text = text.encode(charset).strip()
            return (
                """\n<div class="highlight">
                <pre><code>%s</code></pre>
                </div>\n""" % h.escape_html(text)
            )

        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()

        return highlight(text, lexer, formatter)


renderer = ColorRenderer()

markdown = m.Markdown(
    renderer,
    extensions=m.EXT_FENCED_CODE | m.EXT_NO_INTRA_EMPHASIS | m.EXT_AUTOLINK
)


# method: parse
# input: unicode string( head: toml, body: markdown )
# output: dict(markdown, html, toml-dict-items)
def parse(content):
    lines = content.splitlines()
    l = None

    for lineno, line in enumerate(lines):
        if separator in line:
            l = lineno
            break  # use the first ----

    if not l:
        raise Exception("Separator not found.")

    head, body = "\n".join(lines[:l]), "\n".join(lines[l+1:])

    # parse head
    dct = toml.loads(head)
    # add markdown, html key
    dct["markdown"] = body
    dct["html"] = markdown.render(body)
    return dct
