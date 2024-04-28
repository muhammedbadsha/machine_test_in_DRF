from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
def index(request):
    return HttpResponse('<h1>thsi worked</h1>')


class UserRegistrationView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # @method_decorator(login_required)
    def get(self,request):
        snippets = User.objects.all()
        print(snippets[0])
        serializer = UserRegistrationView(data={
            "user_name":"arshadali",
            "age":13
            }, many=True)
        return JsonResponse(serializer.data, safe=False)
class UserRegistration(APIView):
    def post(self, request):
        data = request.data
        serializer_class = UserRegistrationView(data = data,many=False)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        

        