from django import template

register = template.Library()


@register.filter
def xrange(total, num):
    t = int(total/num)
    if t < total/num:
        return range(t+2)[1:]
    else:
        return range(t+1)[1:]
