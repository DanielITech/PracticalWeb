from django.shortcuts import render
from django.views.generic import DetailView
from .models import Tutorial


class TutorialView(DetailView):
    template_name = 'tutorialsApp/index.html'
    model = Tutorial
    context_object_name = 'tuts'
