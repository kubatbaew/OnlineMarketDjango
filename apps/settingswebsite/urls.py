from django.urls import path

from apps.settingswebsite.views import homepage


urlpatterns = [
    path('', homepage, name='homepage'),
]
