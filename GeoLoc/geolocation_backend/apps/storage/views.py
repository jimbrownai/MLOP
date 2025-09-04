from django.shortcuts import render

# Create your views here.
# apps/storage/views.py
from django.http import JsonResponse

def upload_image(request):
    return JsonResponse({"message": "upload endpoint working"})

def download_dataset(request):
    return JsonResponse({"message": "download endpoint working"})
