from django.urls import path
from .views import TranslateView
app_name = "translate"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('translate/', TranslateView.as_view()),
]