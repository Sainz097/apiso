from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .models import Student
#from .models import collageCareer
from .serializer import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes=(IsAuthenticated,)
    authentication_class=(TokenAuthentication,)


#class StudentListView(viewsets.ModelViewSet):
#    def post(self, request, format=None):
#        nombre=request.data['name']
#        queryset = Student.objects.filter(name__icontains= nombre)
#        serializer = StudentSerializer(queryset, many=True)
#        return Response(serializer.data)   