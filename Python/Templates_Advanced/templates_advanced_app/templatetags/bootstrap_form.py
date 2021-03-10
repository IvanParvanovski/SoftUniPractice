from django import template

register = template.Library()


@register.inclusion_tag('bootstrap_form.html')
def bootstrap_form(form, action, method):
    for (_, field) in form.fields.items():
        if 'class' not in field.widget.attrs:
            field.widget.attrs['class'] = ''
        field.widget.attrs['class'] += ' form-control'

    return {
        'form': form,
        'action': action,
        'method': method
    }
