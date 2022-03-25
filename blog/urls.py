from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("posts", views.ListPostAPIView.as_view()),
    path("post/<int:pk>", views.RetrievePostAPIView.as_view(), name="post-detail")
]