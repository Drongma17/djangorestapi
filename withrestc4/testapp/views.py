from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer

class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
