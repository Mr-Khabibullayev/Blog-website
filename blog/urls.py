from django.urls import path
from .views import BlogLIstView,BlogDetailView, Post_Create_Delete

urlpatterns = [
    path('',BlogLIstView.as_view(),name='home'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path('post/news/',Post_Create_Delete.as_view(), name='post_new')
]
