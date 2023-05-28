from django.urls import path
from . views import GoogleCalendarInitView, GoogleCalendarRedirectView

app_name = 'calendar'

urlpatterns = [
    path('rest/v1/calendar/init/', GoogleCalendarInitView, name='init'),
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView, name='redirect'),
]
