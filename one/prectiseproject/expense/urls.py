from django.urls import path
from . import views


urlpatterns = [
    path('', views.expenses, name='expenses'),
    path('/add', views.add_expense, name='add_expense_url'),
    path('/edit/<int:id>', views.edit_expense, name='edit_expense_url'),
]
