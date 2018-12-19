from django.urls import path

from .views import FormView, FormListView

from . import views

urlpatterns = [
    # ex: /polls/
    path('', FormView.as_view(), name='index'),
    path('list/', FormListView.as_view(), name='formlist'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]