from django import template

register = template.Library()


@register.filter
def snake_filter(snakes, name='Ivan'):
    return [snake for snake in snakes if snake.name == name]
