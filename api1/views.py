from django.shortcuts import render
from rest_framework import viewsets
from api1.models import company,Employee
from api1.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class companyViewSet(viewsets.ModelViewSet):
    queryset= company.objects.all()
    serializer_class=CompanySerializer
    
    
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):   
        try:                
            company=company.objects.get(pk=pk)
            employees=Employee.objects.filter(company=company)
            employees_serializer=EmployeeSerializer(employees,many=True,context={'request':request})
            return Response(employees_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exists !! Error'
            })
    

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
