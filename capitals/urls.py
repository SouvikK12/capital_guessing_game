from django.urls import path
from .views import CapitalApiViewSet


urlpatterns = [
    path('', CapitalApiViewSet.as_view({'post' : 'check_capital', 'get' : 'random_country'})),
]