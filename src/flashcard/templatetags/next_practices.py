# -*- mode: python; coding: utf-8; -*-

"""
Template tag which returns a list of the next practice objects for a given user

How to use in the template:

    {% get_next_practices <quantity> %}

    <quantity> - the number of practice objects to return
"""

__author__ = "Kenny Meyer"
__email__ = "knny.myer@gmail.com"

from django import template

from flashcard.models import FlashCard

register = template.Library()

def do_next_practices(parser, token):
    bits = token.contents.split()
    if len(bits) != 2:
        raise TemplateSyntaxError, \
                "get_next_practices takes exactly one argument: `quantity`."

    quantity = bits[1]
    return NextPracticesNode(quantity)

class NextPracticesNode(template.Node):
    def __init__(self, quantity):
        self.quantity = quantity

    def render(self, context):
        context['next_practices'] = FlashCard.by_practice.all()[self.number]
        return ''

register.tag('get_next_practices', do_next_practices)

# vim: ai ts=4 sts=4 et sw=4
