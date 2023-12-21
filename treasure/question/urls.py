# your_app_name/urls.py
from django.urls import path
from . import views

app_name="question"
urlpatterns = [
    path('submit_answers/', views.submit_answers, name='submit_answers'),
    # Add more URL patterns as needed
]
