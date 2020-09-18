from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('branch', views.BranchView)
router.register('employee', views.EmployeeView)

urlpatterns = [
    path('closest_branch/', views.test_view),
    path('', include(router.urls)),
]
