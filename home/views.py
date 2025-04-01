from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Concert
from datetime import datetime, timedelta
import calendar
import json
from PIL import Image

def printj(json_file):
    """Debugging tool"""
    print(json.dumps(json_file, indent=4))


def home(request):
    concerts = Concert.objects.all()
    concerts_list = [
        {
            "name": concert.name,
            "image": request.build_absolute_uri(concert.image.url) if concert.image else None,
            "date": str(concert.date),
            "venue": concert.venue,
            "description":concert.description,
            "spotify": str(concert.spotify),
            "instagram": str(concert.instagram)
        }
        for concert in concerts
    ]
    
    context = {
        'concerts_json': json.dumps(concerts_list)  # Pass serialized data as JSON
    }
    # printj(context['concerts_json'])
    return render(request, 'home/home.html', context)

def calendar_view(request, year=None, month=None):
    # Default to current month and year if none provided
    today = datetime.today()
    year = year or today.year
    month = month or today.month

    # Calculate the first and last days of the month
    first_day = datetime(year, month, 1)
    last_day = datetime(year, month, calendar.monthrange(year, month)[1])

    # Group dates by rows, with placeholders for missing days
    dates_grid = []
    week_row = [None, None, None]  # Start with an empty row of placeholders

    current_day = first_day
    while current_day <= last_day:
        # Reset the week row for a new row if it's a Thursday
        if current_day.weekday() == 3:  # Thursday starts a new row
            week_row = [None, None, None]

        if current_day.weekday() in [3, 4, 5]:  # Thursday, Friday, Saturday
            concerts = Concert.objects.filter(date__date=current_day.date())
            day_info = {
                'day_name': current_day.strftime('%A'),
                'day_num': current_day.day,
                'date': current_day,
                'concerts': concerts,
            }
            # Place the day_info in the correct column: Thursday (0), Friday (1), Saturday (2)
            week_row[current_day.weekday() - 3] = day_info

            # If it's Saturday, the row is complete; add it to the grid
            if current_day.weekday() == 5:
                dates_grid.append(week_row)

        current_day += timedelta(days=1)

    # If the last row is incomplete (i.e., we don’t end on a Saturday), add it as is
    if any(week_row):
        dates_grid.append(week_row)

    # Calculate next and previous month for navigation
    next_month = 1 if month == 12 else month + 1
    next_year = year + 1 if month == 12 else year
    prev_month = 12 if month == 1 else month - 1
    prev_year = year - 1 if month == 1 else year

    context = {
        'dates_grid': dates_grid,
        'month_name': calendar.month_name[month],
        'year': year,
        'next_month': next_month,
        'next_year': next_year,
        'prev_month': prev_month,
        'prev_year': prev_year,
    }
    return render(request, 'home/calendar.html', context)

def concert_detail(request, concert_id):
    concert = get_object_or_404(Concert, id=concert_id)
    return render(request, 'home/concert_detail.html', {'concert': concert})

def wip(request):
    return render(request, 'home/wip.html', {})