from main.views import PerevalListView, PerevalCreateView, PerevalDeteilView, PhotoListView, \
    PhotoAddView
from django.urls import path, include

urlpatterns = [
    path('pereval/', PerevalListView.as_view()),
    path('pereval/add/', PerevalCreateView.as_view()),
    path('pereval/<int:pk>/', PerevalDeteilView.as_view()),
    path('photos/', PhotoListView.as_view()),
    path('photos/add/', PhotoAddView.as_view()),
    # path('coards/', CoardsListView.as_view()),

]
