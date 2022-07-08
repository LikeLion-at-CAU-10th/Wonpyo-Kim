from django.urls import path
from .views import *
urlpatterns = [
    path('', read_all),
    path('create', create),
    path('<int:id>', read_one),
    path('remove/<int:id>', remove),
    path('update/<int:id>', update)
]