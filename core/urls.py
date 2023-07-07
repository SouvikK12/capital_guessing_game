from django.urls import include, path


urlpatterns = [
    path('countries_and_capitals/', include('capitals.urls')),
]
