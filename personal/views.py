from skill.models import Skill
from personal.models import Project
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Skill

# class HomePageView(TemplateView):
#     model = Project
#     template_name = 'home.html'
#     context_object_name = 'all_projects'

class SkillsPageView(TemplateView):
    model = Skill
    template_name = 'skills.html'
# Create your views here.
