from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='expenses'),
    path('add_expenses',views.add_expenses, name='add_expenses')
]
