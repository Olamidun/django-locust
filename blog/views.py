from django.shortcuts import render

from itsdangerous import Serializer
from .serializers import ListPostSerializer, ListPlainPostSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Post, Comment

# Create your views here.


class ListPostAPIView(ListAPIView):
    serializer_class = ListPostSerializer
    def get_queryset(self):
        posts = Post.objects.select_related('user').all() # select_related is used to prevent django from hitting the db when getting the related user for a post
        return posts
    
    # def list(self, request, *args, **kwargs):
        # queryset = self.get_queryset()
        # data = self.plain_serializer_class.serialize_post(queryset)
        # print(data)
        # return Response(data)
        # # return super().list(request, *args, **kwargs)

class RetrievePostAPIView(RetrieveAPIView):
    serializer_class = ListPostSerializer
    lookup_field = "pk"
    def get_queryset(self):
        return Post.objects.select_related('user').filter(id=self.kwargs.get('pk'))




