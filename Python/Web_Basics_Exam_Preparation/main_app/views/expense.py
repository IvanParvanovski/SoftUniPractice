from django.shortcuts import redirect, render

from main_app.forms.expense import ExpenseForm, DeleteExpenseForm
from main_app.models.expense import Expense
from main_app.views.shared import visualise_view


def create_expense(req):
    if req.method == 'GET':
        form = ExpenseForm()
        return visualise_view(req, form, 'expense-create.html')
    else:
        form = ExpenseForm(req.POST)

        if form.is_valid():
            form.save()
            return redirect('home page')

        return visualise_view(req, form, 'expense-create.html')


def edit_expense(req, pk):
    expense = Expense.objects.get(pk=pk)

    if req.method == 'GET':
        form = ExpenseForm(instance=expense)

        return visualise_view(req, form, 'expense-edit.html', expense=expense)

    else:
        form = ExpenseForm(req.POST,
                           instance=expense)

        if form.is_valid():
            form.save()
            return redirect('home page')

        return visualise_view(req, form, 'expense-edit.html')


def delete_expense(req, pk):
    expense = Expense.objects.get(pk=pk)

    if req.method == 'GET':
        form = DeleteExpenseForm(instance=expense)
        return visualise_view(req, form, 'expense-delete.html', expense=expense)
    else:
        expense.delete()
        [expense.delete() for expense in Expense.objects.all()]
        return redirect('home page')
