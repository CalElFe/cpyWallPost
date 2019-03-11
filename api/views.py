# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api.models import Post
from api.serializers import PostSerializer
from .utils import *


@csrf_exempt
def post_request(request, id):
    try:
        post = Post.objects.get(post_id=id)
        context = {}
        context['post_id'] = post.post_id
        context['post_data'] = post.post_data
        return render(request, 'index.html', context)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

@csrf_exempt
def post_add(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        if 'post_data' in data:
            hash = calcHash(data['post_data'])
            data['post_uniqueCode'] = hash
        else:
            return HttpResponse("Bad syntax", status=400)

        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            try:
                post = Post.objects.get(post_uniqueCode=data['post_uniqueCode'])
                if post != None:
                    return HttpResponse("post with requested code already exists", status=409)
            except Post.DoesNotExist:
                serializer.save()
                id = serializer.data['post_id']
                return HttpResponse(str(id), status=200)
        else:
            return HttpResponse("Bad syntax", status=400)
    else:
        return HttpResponse(status=404)

@csrf_exempt
def post_edit(request, id):
    if request.method == 'PUT':
        try:
            post = Post.objects.get(post_id=id)
            data = JSONParser().parse(request)
            if 'post_data' in data:
                hash = calcHash(data['post_data'])
                if post.post_uniqueCode != hash:
                    post.post_data = data["post_data"]
                    post.post_uniqueCode = hash
                    post.save()
                else:
                    return HttpResponse("Same with the one on server", status=409)
                return HttpResponse(status=200)
            else:
                return HttpResponse("Bad syntax", status=400)
        except Post.DoesNotExist:
            return HttpResponse("Requested post does not exist", status=410)
    else:
        return HttpResponse(status=404)

@csrf_exempt
def post_del(request, id):
    if request.method == 'DELETE':
        try:
            post = Post.objects.get(post_id=id)
            post.delete()
            return HttpResponse(status=200)
        except Post.DoesNotExist:
            return HttpResponse("Requested post does not exist", status=410)
    else:
        return HttpResponse(status=404)

@csrf_exempt
def post_get_QR(request, id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(post_id=id)
            context = {}
            context['post_id'] = id
            context['post_data'] = generateQR(id)
            return render(request, 'index.html', context)
        except Post.DoesNotExist:
            return HttpResponse("Requested post does not exist", status=410)
    else:
        return HttpResponse(status=404)
