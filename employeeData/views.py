from django.shortcuts import render
import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .serializers import EmployeeSerializer
from .models import Employee

class EmployeeUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        file = request.data['file']
        # Handle validations and error cases as needed

        # Process the CSV file and populate the database
        data = self.parse_csv(file)
        serializer = EmployeeSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'CSV data imported successfully'})
        else:
            return Response(serializer.errors, status=400)

    def parse_csv(self, file):
        data = []
        decoded_file = file.read().decode('utf-8')
        csv_reader = csv.DictReader(decoded_file.splitlines())
        for row in csv_reader:
            employee = {
                'first_name': row['FirstName'],
                'last_name': row['LastName'],
                'email': row['Email'],
                'phone': row['Phone'],
                'gender': row['Gender'],
                'department': row['Department'],
                'job_title': row['JobTitle'],
                'years_of_experience': int(row['YearsOfExperience']),
                'salary': float(row['Salary'])
            }
            data.append(employee)
        return data

class EmployeeListView(APIView):
    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
