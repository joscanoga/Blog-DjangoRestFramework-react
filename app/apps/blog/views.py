from django.shortcuts import render, get_object_or_404
from rest_framework import  status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from .pagination import SmallSetPagination, MediumSetPagination, LargeSetPagination

class BlogListView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        if Post.postobjects.all().exists():
            posts = Post.postobjects.all()
            paginator = SmallSetPagination()
            result_page = paginator.paginate_queryset(posts, request)
            serializer = PostSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({'message': 'No Blog Found'}, status=status.HTTP_404_NOT_FOUND)
        
class PostDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)
