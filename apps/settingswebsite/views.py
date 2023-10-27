from django.shortcuts import render

from apps.settingswebsite.models import SettingsWebsite


def homepage(request):
    settings_website = SettingsWebsite.objects.get(id=1)

    return render(request, 'index.html', locals())
