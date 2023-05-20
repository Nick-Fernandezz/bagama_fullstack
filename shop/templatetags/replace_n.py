from django import template

register = template.Library()

@register.filter(is_safe = True)
def replace_n(value):
    value = '<p>' + value + '</p>'
    return value.replace('\n', '</p><p>')
