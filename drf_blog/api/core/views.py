from rest_framework import viewsets
from .serializers import PostSerializer
from rest_framework.response import Response

from .models import *


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'