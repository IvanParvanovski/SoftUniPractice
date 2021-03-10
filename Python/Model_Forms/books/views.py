from django.shortcuts import render, redirect

from books.forms import BookForm
from books.models import Book


def index(req):
    context = {
        'books': Book.objects.all()
    }
    return render(req, 'index.html', context=context)


def create_form(req):
    # Return empty form when req is GET
    if req.method == 'GET':

        context = {
            'form': BookForm(),
        }

        return render(req, 'create.html', context=context)

    # Save user's form into the database

    # Fill in the form
    form = BookForm(req.POST)

    # If the data is valid save to database
    if form.is_valid():
        form.save()
        return redirect('books index')

    # Else return the form with user's info + errors

    context = {
        'form': form,
    }

    return render(req, 'create.html', context=context)


def edit_form(req, pk):
    book = Book.objects.get(pk=pk)

    if req.method == 'GET':
        form = BookForm(instance=book)

        context = {
            'form': form
        }

        return render(req, 'edit.html', context=context)

    # Not creating new form
    # Changing the old one (instance=book)
    # Rewrite the data of book
    form = BookForm(req.POST, instance=book)

    if form.is_valid():
        form.save()
        return redirect('books index')

    context = {
        'form': form,
    }

    return render(req, 'edit.html', context=context)


# ===============================================
#                 Summary funcs
# ===============================================


def create_form2(req):
    return persist(req, Book(), 'create')


def edit_form2(req, pk):
    return persist(req, Book.objects.get(pk), 'edit')


def persist(req, book, template_name):
    if req.method == 'GET':
        context = {
            'form': BookForm(instance=book)
        }

        return render(req, template_name, context=context)

    form = BookForm(req.POST, instance=book)

    if form.is_valid():
        form.save()
        return redirect('books index')

    context = {
        'form': form,
    }

    return render(req, template_name, context=context)
