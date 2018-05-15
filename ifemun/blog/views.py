from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Post

import requests
import json


def str_hook(obj):
    return {k.encode('utf-8') if isinstance(k,unicode) else k :
            v.encode('utf-8') if isinstance(v, unicode) else v
            for k,v in obj}


class PostList(TemplateView):
    def get(self, request, **kwargs):
        # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        r = requests.get('http://127.0.0.1:8000/blog/api')
        r.encoding = 'ascii'
        posts = json.loads(r.text, object_pairs_hook=str_hook)
        template_path = "blog/post_list.html"
        return render(request, template_path, {'posts': posts})


class PostDetail(TemplateView):
    def get(self, request, **kwargs):
        pk = kwargs.get('pk')
        # post = get_object_or_404(Post, pk=pk)
        r = requests.get('http://127.0.0.1:8000/blog/api', params={'id': pk})
        r.encoding = 'ascii'
        post = json.loads(r.text, object_pairs_hook=str_hook)
        template_path = "blog/post_detail.html"
        return render(request, template_path, {'post': post})