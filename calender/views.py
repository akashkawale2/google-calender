from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from google.auth import exceptions
from google.oauth2 import credentials

# 1. GoogleCalendarInitView
def GoogleCalendarInitView(request):
    # Redirect user to Google OAuth consent screen
    return HttpResponseRedirect(reverse('calendar_integration:redirect'))

# 2. GoogleCalendarRedirectView
def GoogleCalendarRedirectView(request):
    # Handle the redirect request sent by Google
    code = request.GET.get('code')

    # Exchange the authorization code for an access token
    try:
        # Replace 'CLIENT_ID', 'CLIENT_SECRET', and 'REDIRECT_URI' with your own values
        credentials_info = credentials.Credentials.from_client_code(
            client_id='371751789967-48qtmbeco92mdj6smp29o6tvof2pqd9t.apps.googleusercontent.com',
            client_secret='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',
            code=code,
            redirect_uri='http://localhost:8000/rest/v1/calendar/redirect/',
        )
        access_token = credentials_info.token
    except exceptions.GoogleAuthError:
        # Handle any exceptions that may occur during token retrieval
        return HttpResponse('Error: Unable to retrieve access token.')

    # Use the access token to get a list of events in the user's calendar
    # Replace this code with your own implementation to fetch events

    return HttpResponse('Access Token: ' + access_token)
