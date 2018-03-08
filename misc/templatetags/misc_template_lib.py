from django import template

from django.template import defaultfilters


register = template.Library()


@register.filter(name="float_format_0_2")
def float_format_0_2(value, arg=None):

    zero_ = "-"
    format_ = "-2"

    if arg:
        args_ = [a_ for a_ in arg.split(",")]
        len_ = len(args_)
        if len_ >= 1: zero_ = args_[0]
        if len_ >= 2: format_ = args_[1]

    if not value: return zero_
    return defaultfilters.floatformat(value, format_)
