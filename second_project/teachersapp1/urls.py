
from django.urls import path
from .views import teacher_list
from .views import teacher_details
urlpatterns = [

    path('list',teacher_list),
    path('details/<int:code>',teacher_details)
]