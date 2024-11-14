from django.shortcuts import render
from .models import Concert
import json

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
