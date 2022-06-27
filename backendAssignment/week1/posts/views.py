from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def json_response(request):
    dict = {"assignment" : "is difficult"}
    if request.method == "GET":
        return JsonResponse(dict)