from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Post
from .serializers import PostSerializer

import json


class PostList(TemplateView):
    def get(self, request, **kwargs):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        template_path = "blog/post_list.html"
        return render(request, template_path, {'posts': posts})

class PostDetail(TemplateView):
    def get(self, request, **kwargs):
        pk = kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk)
        template_path = "blog/post_detail.html"
        return render(request, template_path, {'post': post})

class Api(TemplateView):
    def get(self, request, **kwargs):
        post_id = request.GET.get('id')
        if not post_id:
            posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            serializer = PostSerializer(posts, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            post = get_object_or_404(Post, pk=post_id)
            serializer = PostSerializer(post, many=False)
            return JsonResponse(serializer.data, safe=False)
