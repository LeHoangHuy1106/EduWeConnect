from django.urls import path
from .views import AddSubjectAPIView, ListSubjectsAPIView, DeleteSubjectAPIView

urlpatterns = [
    path('add-subject/', AddSubjectAPIView.as_view(), name='add-subject'),
    path('list-subjects/', ListSubjectsAPIView.as_view(), name='list-subjects'),
    path('delete-subject/<str:id_subject>/', DeleteSubjectAPIView.as_view(), name='delete-subject'),
]