from django.shortcuts import render


def visualise_view(req, form, template_name, **kwargs):
    context = {
        'form': form,
    }

    for (key, value) in kwargs.items():
        context[key] = value

    return render(req, f'{template_name}', context=context)
