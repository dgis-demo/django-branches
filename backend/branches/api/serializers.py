from rest_framework import serializers
from branches.models import Branch, Employee


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('name', 'facade', 'latitude', 'longitude')


class EmployeeSerializer(serializers.ModelSerializer):
    branch = serializers.CharField()

    class Meta:
        model = Employee
        fields = ('branch', 'last_name', 'first_name', 'position')
