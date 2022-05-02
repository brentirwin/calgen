# Generate a and b dates for the school year.

def gen_dates():
    import datetime
    import pprint

    # Constants
    START_DATE = (2022, 1, 5)
    END_DATE = (2022, 5, 20)
    EXEMPT_DATES = ((2022, 1, 17),
                    (2022, 2, 22),
                    (2022, 3, 11),
                    (2022, 3, 14),
                    (2022, 3, 15),
                    (2022, 3, 16),
                    (2022, 3, 17),
                    (2022, 3, 18),
                    (2022, 4, 15))

    # Convert constants to dates/arrays of dates
    sdate = datetime.date(*START_DATE)
    edate = datetime.date(*END_DATE)
    delta = edate - sdate
    exempt_dates = [datetime.date(*day) for day in EXEMPT_DATES]

    # Initialize variables for loop
    a_day = True
    date_list = []

    # For each date in the range,
    for i in range(delta.days + 1):
        day = sdate + datetime.timedelta(days=i)
        # If the date is not an exempt date, adn it's a weekday
        # Add the date and a/b day to the list.
        if day not in exempt_dates and day.weekday() in range(5):
            date_list.append((day, a_day))
            a_day ^= True

    # pprint.pprint(date_list)

    # Create all events for a day
    def create_events(day, a_day):
        day = day.strftime('%Y-%m-%d') + 'T'

        # Create a single event
        def create_event(day, summary, start, end):
            return {
                'summary': summary,
                'start': {
                    'dateTime': day + start + ':00',
                    'timeZone': 'America/Chicago',
                },
                'end': {
                    'dateTime': day + end + ':00',
                    'timeZone': 'America/Chicago',
                }
            }
        # For A days, periods 1, 3A, 3B, and 4
        if a_day:
            events = [create_event(day, 'Adv CS 1 - 1', '09:05', '10:35'),
                      create_event(day, 'Adv CS 1 - 3', '12:21', '13:20'),
                      create_event(day, 'Adv CS 1 - 3', '14:03', '14:34'),
                      create_event(day, 'Adv CS 1 - 4', '14:42', '16:20')]
        # For B days, periods 5, 6, 7A, and 7B
        else:
            events = [create_event(day, 'AP CS A - 5', '09:05', '10:35'),
                      create_event(day, 'AP CS A - 6', '10:43', '12:14'),
                      create_event(day, 'AP CS A - 7', '12:21', '13:20'),
                      create_event(day, 'AP CS A - 7', '14:03', '14:34')]
        return events

    # Create a list of events for each day in the range.
    all_events = []
    for day, a_day in date_list:
        all_events += create_events(day, a_day)

    return all_events

