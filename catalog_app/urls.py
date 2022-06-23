from django.urls import path

from . import views

urlpatterns = [
    path('processor/', views.ProcessorView.as_view(), name='processor'),
    path('videocard/', views.VideocardView.as_view()),
    path('motherboard/', views.MotherboardView.as_view()),
    path('ram/', views.RAMView.as_view()),
    path('case/', views.CaseView.as_view()),
    path('cooler/', views.CoolerView.as_view()),
    path('hdd/', views.HDDView.as_view()),
    path('powerunit/', views.PowerunitView.as_view())
]
