
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Announcement
from .serializers import AnnouncementSerializer


class AnnouncementCreateView(APIView):
    def post(self, request):
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnnouncementListView(APIView):
    def get(self, request):
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)