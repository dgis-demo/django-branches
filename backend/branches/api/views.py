from django.contrib.gis.geos import GEOSGeometry
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from branches.models import Branch, Employee
from .serializers import BranchSerializer, EmployeeSerializer


class BranchView(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name']
    ordering_fields = ['name']


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['branch__name', 'branch']
    ordering_fields = ['branch', 'branch__name', 'first_name', 'last_name', 'position']


@api_view(['GET'])
def test_view(request):
    params = request.query_params
    if 'lat' and 'lon' in params:
        if params['lat'] and params['lon']:
            lat = int(params['lat'])
            lon = int(params['lon'])
            target_point = GEOSGeometry(f'SRID=4326;POINT({lon} {lat})')
            distances = dict()
            for branch in Branch.objects.all():
                branch_point = GEOSGeometry(f'SRID=4326;POINT({branch.longitude} {branch.latitude})')
                distance = target_point.distance(branch_point)
                distances[distance] = branch.pk
            min_distance = min(distances.keys())
            closest_branch = Branch.objects.get(pk=distances[min_distance]).to_json()
            return Response(closest_branch, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
