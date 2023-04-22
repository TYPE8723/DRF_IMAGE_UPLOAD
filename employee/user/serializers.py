from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','name','email','photo')
        read_only_fields = fields
        #use "read_only_fields" incase if get method is ony used.