from django.shortcuts import render
from itsdangerous import Serializer
from .serializers import ListPostSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post, Comment

# Create your views here.


class ListPostAPIView(ListAPIView):
    serializer_class = ListPostSerializer
    def get_queryset(self):
        posts = Post.objects.select_related('user').all()
        return posts

class RetrievePostAPIView(RetrieveAPIView):
    serializer_class = ListPostSerializer
    lookup_field = "pk"
    def get_queryset(self):
        return Post.objects.select_related('user').filter(id=self.kwargs.get('pk'))




