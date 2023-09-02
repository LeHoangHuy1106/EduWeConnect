from django.urls import path

from advise.views import DataScore

urlpatterns = [
    path('data/<str:code>/', DataScore.as_view(), name='data-collect'),
]