from django.urls import path
from .views import BlogLIstView

urlpatterns = [
    path('',BlogLIstView.as_view(),name='home')
]
