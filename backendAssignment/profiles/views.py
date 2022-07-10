from django.http import JsonResponse
import json

from django.shortcuts import get_object_or_404

from .models import *
from django.core.serializers import serialize
# Create your views here.

def create(request):
    
    if request.method == "POST":
        body = json.loads(request.body)
        
        new_profile = Profile.objects.create(
            name = body["name"],
            age = body["age"],
            phone = body["phone"]
        )

        new_profile_json = {
            "name" : new_profile.name,
            "age" : new_profile.age,
            "phone" : new_profile.phone
        }

        return JsonResponse({
            "status": 200,
            "success" : True,
            'message' : '생성 성공',
            'data': new_profile_json
        })
    return JsonResponse({
        "status": 405,
        "success" : False,
        'message' : '데이터 보내줘라',
        'data': None
    })
            
def read_all(request):
    if request.method == "GET":
        profiles = Profile.objects.all().order_by("id")
        
        data = json.loads(serialize('json', profiles))
        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "조회 성공",
            "data": data
        })
    return JsonResponse({
        "status" : 405,
        "success" : False,
        "message" : "조회만 가능합니다",
        "data": None
    })

def read_one(request,id):
    if request.method == "GET":
        profile = get_object_or_404(Profile,pk = id)
        data = {
            "name" : profile.name,
            'age' : profile.age,
            'phone' : profile.phone
        }
        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "조회 성공",
            "data" : data
        })
            
    return JsonResponse({
        "status" : 405,
        "success" : False,
        "message" : "GET으로만 보내세요",
        "data": None
    })
def remove(request, id):
    if request.method == "POST":
        profile = get_object_or_404(Profile, pk = id)
        data = {
            "name" : profile.name,
            "age" : profile.age,
            "phone" : profile.phone
        }
        profile.delete()
        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "삭제 완료",
            "data" : data
        })
    return JsonResponse({
        "status" : 406,
        "success" : False,
        "message" : "POST로만 보내세요",
        "data" : None
    })
def update(request, id):
    if request.method == "POST":
        profile = get_object_or_404(Profile, pk = id)
        profile.delete()
        body = json.loads(request.body)
        Profile.objects.create(
            id = id,
            name = body["name"],
            age = body['age'],
            phone = body['phone']
        )   
       
        
        data = {
            "name" : profile.name,
            "age" : profile.age,
            "phone" : profile.phone
        }
        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "update 성공",
            "data" : data
        })
    return JsonResponse({
        "status" : 406,
        "success" : False,
        "message" : "POST로만 보내세요",
        "data" : None
    })