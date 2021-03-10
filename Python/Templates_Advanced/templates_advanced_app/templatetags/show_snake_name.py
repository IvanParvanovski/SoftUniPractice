from django import template

register = template.Library()


@register.simple_tag()
def snake_name(name):
    return f'<h5 class="card-title">{name}</h5>'
