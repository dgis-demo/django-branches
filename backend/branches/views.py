from django.shortcuts import render
from django.http.response import JsonResponse


def index_view(request):
    return render(request, 'index.html')
    # return JsonResponse({1: 1})
