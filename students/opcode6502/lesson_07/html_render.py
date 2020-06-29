#!/usr/bin/env python3
#
# html_render.py
# opcode6502: SP_Online_PY210
"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.contents = content
        if self.contents is None:
            self.contents = []
        else:
            self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        #
        # Opening <tag>.
        open_tag = ["<{}".format(self.tag)]
        #
        # Add the attributes.
        for key, value in self.attributes.items():
            open_tag.append(' {}="{}"'.format(key, value))
        #
        # Finish writing the opening <tag>.
        open_tag.append(">\n")
        out_file.write("".join(open_tag))
        #
        # Write the content.
        for content in self.contents:
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content +'\n')
        #
        # Closing </tag>.
        out_file.write('</{}>\n'.format(self.tag))


class Body(Element):
    tag = 'body'


class Head(Element):
    tag = 'head'


class Hr(SelfClosingTag):
    tag = 'hr'


class Html(Element):
    tag = 'html'


class OneLineTag(Element):

    def render(self, out_file):
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))

    def append(self, content):
        raise NotImplementedError


class P(Element):
    tag = 'p'


class SelfClosingTag(Element):

    def render(self, outfile):
    # put rendering code here.


class Title(OneLineTag):
    tag = 'title'
