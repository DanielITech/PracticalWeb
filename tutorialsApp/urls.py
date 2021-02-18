from django.urls import path
from .views import TutorialView

urlpatterns = [
    path('<slug:slug>/',TutorialView.as_view(), name='tutorial_url'),
]
