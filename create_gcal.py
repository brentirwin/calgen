from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import gen_dates

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.events']

# Calendar ID for Class calendar
CALENDAR_ID = 'c_u3qrj4okijfn7fp0s8t3f9guhc@group.calendar.google.com'

def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'token.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    ''' test code: event = {'summary': 'Test',
             'start': {'dateTime': '2021-11-06T10:00:00',
                       'timeZone': 'America/Chicago'},
             'end': {'dateTime': '2021-11-06T11:00:00',
                     'timeZone': 'America/Chicago'}
             }
'''
    events = gen_dates.gen_dates()
    events_created = 0
    for event in events:
        event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
        events_created += 1

    print(events_created, 'events created! You did it! Congratulations, Mr. Irwin.')
if __name__ == '__main__':
    main()
