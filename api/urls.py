from django.urls import path
from django.http import HttpResponse
from .views import HealthDataListCreate

def test_view(request):
    return HttpResponse("Test route working!")

urlpatterns = [
    path('health-data/', HealthDataListCreate.as_view(), name='health-data'),
    path('test/', test_view, name='test'),
]