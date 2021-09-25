from django.contrib.admin.sites import all_sites
from django.urls import path
from .views import ContactPageView, HomePageView, SkillsPageView
urlpatterns = [
    path('skills/', SkillsPageView.as_view(), name='skills'),
    path('', HomePageView.as_view(), name='home'),
]