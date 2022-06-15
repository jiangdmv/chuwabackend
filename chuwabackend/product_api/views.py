from rest_framework import generics, viewsets, filters, generics, permissions
from product.models import PostProduct
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

# Display Posts

class PostList(generics.ListAPIView):

    queryset = PostProduct.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):

    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(PostProduct, id=item)


# Post Search

class PostListDetailfilter(generics.ListAPIView):

    queryset = PostProduct.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['^slug']


# Post Admin

class CreatePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PostProduct.objects.all()
    serializer_class = PostSerializer

class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PostProduct.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PostProduct.objects.all()
    serializer_class = PostSerializer

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PostProduct.objects.all()
    serializer_class = PostSerializer


""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
