from django.urls import path
from .views import ( 
    BlogLIstView,
    BlogDetailView, 
    Post_Create_Delete,
    Blog_Update_View,
    Blog_Delete_View,)

urlpatterns = [
    path('',BlogLIstView.as_view(),name='home'),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path('post/news/',Post_Create_Delete.as_view(), name='post_news'),
    path('post/<int:pk>/edit',Blog_Update_View.as_view(),name="post_edit"),
    path('post/<int:pk>/delete',Blog_Delete_View.as_view(),name='post_delete')
]
