from django.urls import path
from .views import *
urlpatterns = [
    path('sign_up', sign_up, name='sign_up'),
    path('sign_in', sign_in, name='sign_in'),
    path('activate', activate, name='activate'),
    path('sign_out', sign_out, name='sign_out'),
]