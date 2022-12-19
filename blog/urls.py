from django.urls import path
from .views import BlogLIstView,BlogDetailView

urlpatterns = [
    path('',BlogLIstView.as_view(),name='home'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail")
]
