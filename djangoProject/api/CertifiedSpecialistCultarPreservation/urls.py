from django.urls import path
from .views.MainView import MainView
from .views.SingleView import SingleView

urlpatterns = [
    path(r'getMany', MainView.as_view()),
    path(r'<int:id>', SingleView.as_view()),
]