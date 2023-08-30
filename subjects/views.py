from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subject
from .permissions import CanAddSubject
from .serializers import SubjectSerializer

class AddSubjectAPIView(APIView):
    permission_classes = [CanAddSubject]
    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            current_subject_count = Subject.objects.count()
            id_subject = f"sub{current_subject_count + 1:03}"
            serializer.validated_data['id_subject'] = id_subject
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListSubjectsAPIView(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteSubjectAPIView(APIView):
    def delete(self, request, id_subject):
        try:
            subject = Subject.objects.get(id_subject=id_subject)
            subject.delete()
            return Response({"message": "Subject deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Subject.DoesNotExist:
            return Response({"message": "Subject not found."}, status=status.HTTP_404_NOT_FOUND)
