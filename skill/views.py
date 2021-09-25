from typing import List
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Skill

class SkillsPageView(ListView):
    model = Skill
    template_name = 'skills.html'
    context_object_name = 'all_skills_list'
# Create your views here.
