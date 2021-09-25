from typing import List
from django.shortcuts import render
from .models import Project
from django.views.generic import TemplateView, ListView
class HomePageView(ListView):
    model = Project
    template_name = 'home.html'
    context_object_name = 'all_projects_list'

class SkillsPageView(TemplateView):
    template_name = 'skills.html'
# Create your views here.
