# -*- encoding: utf-8 -*-
from django import template
from classytags.core import Tag

register = template.Library()

class RestartStatus(Tag):
    name = 'restart_status'

    def render_tag(self, context):
        status = True
        context['restart_status'] = status
        return ''

register.tag(RestartStatus)
        
# The code below is taken from django.contrib.humanize.naturaltime to ensure
# compatibility with older versions of Django
@register.filter
def naturaltime(value):
    try:
        from django.contrib.humanize.templatetags.humanize import naturaltime as djangonaturaltime
        return djangonaturaltime(value)
    except:
        return u"%s" % value
