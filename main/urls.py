from main.views import CoardsListView, PerevalListView
from django.urls import path, include


urlpatterns = [
    path('', PerevalListView.as_view()),
    path('coards/', CoardsListView.as_view()),


]
