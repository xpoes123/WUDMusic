from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('calendar/<int:year>/<int:month>/', views.calendar_view, name='calendar_month'),
    path('concert/<int:concert_id>/', views.concert_detail, name='concert_detail'),
    path('venues', views.venues, name='venues'),
    path('show_mix', views.show_mix, name='show_mix'),
    path('ad_picks', views.ad_picks, name='ad_picks'),
    path('wud_playlist', views.wud_playlist, name='wud_playlist'),
    path('photos', views.photos, name='photos'),
    path('submit_photos', views.submit_photos, name='submit_photos'),
    path('faq', views.faq, name='faq'),
    path('meetings', views.meetings, name='meetings'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('wip', views.wip, name='wip'),
]