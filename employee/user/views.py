from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get']
    #to perform all opertions using all method
    #Note Remove "read_only_fields" from EmployeeSerializer
    #http_method_names = ['get','post','put','delete']
