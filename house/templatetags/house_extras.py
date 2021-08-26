from django.template.defaultfilters import Library
from django.template.exceptions import TemplateSyntaxError

register = Library()


def multiply(value, arg):
    try:
        return int(value) * int(arg)
    except TemplateSyntaxError:
        return ''


register.filter(name='multiply', filter_func=multiply)
