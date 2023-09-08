import random
import string

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

from users.models import Student, Teacher
from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackCreateView(APIView):

    def post(self, request, username_student):
        # Get the student object using the username
        try:
            student_user = User.objects.get(username=username_student)
            student = Student.objects.get(user=student_user)
        except User.DoesNotExist:
            return Response({'error': 'Student with provided username not found.'}, status=status.HTTP_400_BAD_REQUEST)

        # Assume the teacher is the logged-in user
        teacher = Teacher.objects.get(user=request.user)
        feedback_id = "cmt" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

        # Create the feedback
        feedback_data = {
            "feedback_id": feedback_id,
            'teacher': teacher.id,
            'student': student.id,
            'posted_date': request.data.get('posted_date'),
            'content': request.data.get('content')
        }

        serializer = FeedbackSerializer(data=feedback_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedbackListView(APIView):

    def get(self, request):
        username = request.user.username

        if username.startswith("hs"):
            # user is a student
            student = Student.objects.get(user=request.user)
            feedbacks = Feedback.objects.filter(student=student)

        elif username.startswith("gv"):
            # user is a teacher
            teacher = Teacher.objects.get(user=request.user)
            feedbacks = Feedback.objects.filter(teacher=teacher)

        else:
            return Response({"error": "Invalid user role."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)