from django.urls import path
from .views import HomePageView, SkillsPageView

urlpatterns = [
    path('skill/', SkillsPageView.as_view(), name='skill'),
    path('', HomePageView.as_view(), name='home'),
]