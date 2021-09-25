from django.urls import path
from .views import SkillsPageView

urlpatterns = [
    path('', SkillsPageView.as_view(), name='skills')
]