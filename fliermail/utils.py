from django.template import Template, Context


def render(src, request=None, **kwargs):
    return Template(src).render(Context(kwargs))
