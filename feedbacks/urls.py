from django.urls import path

from feedbacks.views import FeedbackListView

urlpatterns = [
    path('', FeedbackListView.as_view(), name='feedback-list'),
]
