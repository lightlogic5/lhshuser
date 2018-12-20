from django.urls import path

from .views import UserView

urlpatterns = [
    # ex: /polls/
    path('', UserView.as_view(), name='UserView'),
]