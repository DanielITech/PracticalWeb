from django.urls import path
from .views import TutorialView

urlpatterns = [
    path('<int:pk>/',TutorialView.as_view(), name='tutorial_url'),
]
