from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Tutorial


class TutorialView(DetailView):
    template_name = 'tutorialsApp/index.html'
    # queryset = Tutorial.objects.filter(title=DetailView.kwargs['title'])
    context_object_name = 'tut'

    def get_slug_field(self):
        return 'title'

    def get_queryset(self):
        return Tutorial.objects.filter(title=self.kwargs['slug'])
