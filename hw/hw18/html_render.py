#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    def __init__(self, content='', name='', style='', link=''):
        self.name = name
        self.content = content
        self.children = []
        self.style = style
        self.link = link

    def append(self, child):
        self.children.append(child)

    def render(self, f):
        if self.style == '' and self.link == '':
            f.write(" \n     <{name}>".format(name=self.name))
        elif self.style == '' and self.link != '':
            f.write(" \n     <{name} href= '"'{link}'"'>".format
                    (name=self.name, style=self.link))
        else:
            f.write(" \n     <{name} style= '"'{style}'"'' href= '"'{link}'"'>"
                    .format(name=self.name, style=self.style, link=self.link))
        if self.children == []:
            f.write(self.content)
        else:
            for items in self.children:
                items.render(f)
                f.write("\n</{name}>".format(name=self.name))


class Html(Element):
    def __init__(self, content='', style=''):
        Element.__init__(self, content='', style=style, name='html')


class Body(Element):
    def __init__(self, content='', style=''):
        Element.__init__(self, content='', style=style, name='body')


class P(Element):
    def __init__(self, content='', style=''):
        Element.__init__(self, content=content, style=style, name='p')


class Head(Element):
    def __init__(self, content='', style=''):
        Element.__init__(self, content=content, style=style, name='head')


class Title(Element):
    def __init__(self, content='', style=''):
        Element.__init__(self, content=content, style=style, name='title')


class Hr(Element):
    def __init__(self, content='', style=''):
        Element.__init__(self, content=content, style=style, name='title')


class A(Element):
    def __init__(self, link='', content='', style=''):
        Element.__init__(self, content=content, link=link, style='', name='A')
