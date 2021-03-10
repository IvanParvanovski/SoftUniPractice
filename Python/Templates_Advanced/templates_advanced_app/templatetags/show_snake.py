from django import template

register = template.Library()


@register.inclusion_tag('show_pythons.html')
def show_snake(snake):
    return {
        'python': snake,
        'something_else': '',
    }
