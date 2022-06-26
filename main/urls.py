from main.views import *
from django.urls import path, include

from rest_framework import routers
pereval_router = routers.DefaultRouter()
areas_router = routers.DefaultRouter()


pereval_router.register(r'pereval', PerevalView)
areas_router.register(r'areas', AreasView)

urlpatterns = [
    # path('pereval/', PerevalView.as_view({"get": "list"})),
    # path('pereval/add/', PerevalView.as_view({"post": "create"})),
    # path('pereval/<int:pk>/', PerevalView.as_view({"get": "retrieve"})),
    # path('pereval/<int:pk>/update/', PerevalView.as_view({'put': 'update'})),
    path("", include(pereval_router.urls)),
    path("", include(areas_router.urls)),
    path('photos/', PhotoListView.as_view()),
    path('photos/<int:pk>/', PhotoDeteilView.as_view()),
    path('photos/add/',  PhotoAddView.as_view({'post': 'create'})),
    path('users/', UsersListView.as_view()),
    path('users/<int:pk>/', UserDeteilView.as_view()),
    path('users/add/', UserAddView.as_view({'post': "create"})),

    path('add-user-to-pereval/', PerevalUserAddView.as_view()),
    path('pereval-user/', PerevalUsersListView.as_view()),

    # path('coards/', CoardsListView.as_view()),

]
