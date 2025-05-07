from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm



def expenses(request):
    # return HttpResponse("Hello, world. You're at the expense index.")

    allExpense = Expense.objects.all()
    # return HttpResponse(allExpense)

    return render(request, 'expenses.html', {'allExpense': allExpense})


def add_expense(request):
    form = ExpenseForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('expenses')

    return render(request, 'add_expense.html', {'expForm': form})


def edit_expense(request, id):
    exp = get_object_or_404(Expense, id=id)
    form = ExpenseForm(request.POST or None, instance=exp)
    if form.is_valid():
        form.save()
        return redirect('expenses')

    return render(request, 'add_expense.html', {'expForm': form})