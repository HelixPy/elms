from django.urls import path; from django.contrib import admin
from . import views; 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('public_search/<str:keyword>', views.public_search, name='public_search'),
    path('private_search/<str:keyword>', views.private_search, name='private_search'),
    path('publications', views.publications, name='publications'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('bookupload', views.bookupload, name='bookupload'),
    path('login', views.login, name='login'),
    path('uplaod', views.uplaod, name='uplaod'),
    path('public_message', views.public_message, name='public_message'),
    path('private_message', views.private_message, name='private_message'),
    path('leasing/<str:user_id>/<str:book_id>', views.leasing, name='leasing'),
    # path('patientProfile', views.patientProfile, name='patientProfile'),
    # path('frontDesk', views.frontDesk, name='frontDesk'),
    # path('appointment', views.appointment, name='appointment'),
    # path('bloodBank', views.bloodBank, name='bloodBank'),
    # path('login', views.login, name='login'),
    # path('bloodRecord', views.bloodRecord, name='bloodRecord'),
    # path('bloodRecordView', views.bloodRecordView, name='bloodRecordView'), #make dynamic
    # path('search/<str:id>', views.search, name='search'), #enter ID to search for staff or patient

]
# handler404 = "elib.views.handler404"