from django.urls import path

from . import views as v

urlpatterns = [
    path("", v.ListTodo.as_view()),
    path("<int:pk>/", v.DetailTodo.as_view()),
]
