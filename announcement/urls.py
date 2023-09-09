from django.urls import path
from .views import AnnouncementListView, AnnouncementCreateView

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announcement-list'),
    path('add/', AnnouncementCreateView.as_view(), name='announcement-add'),
    # ... your other url patterns
]
