
# week1

![2022-06-27 (7)](https://user-images.githubusercontent.com/69501435/175920511-c94d1990-12df-4c39-ba7e-db89bafded26.png)

1. 가상환경 설정하기 (python -m venv ~)
2. 가상환경 실행시키기 ( ~/Scripts/activate)
3. 장고 설치 (pip install django)
4. django-admin startproject ~ .
5. django-admin startapp ~
6. settings.py에서 secretkey, installedapps 설정하기
7. views 연결 및 urls에 path연결

# week2

### create
```python
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
           
```
create의 경우 db에 수정사항이 생기는 post의 요청이다.
클라이언트는 name, age, phone이 json형태로 데이터를 전송할 것이다. 그러면 서버는 이를 json으로 읽고 
Profile.objects.create()의 함수로 db에 저장을 하고, 데이터 저장에 성공했다고 클라이언트쪽에 전송 할 것이다.
![image](https://user-images.githubusercontent.com/69501435/178146056-ab330be3-e1bb-4ecb-a8a4-07a7d6bad047.png)


### read_all
```python
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
```
db에있는 모든 데이터를 조회 하는 함수이다. Profile.objects.all()로 들고 올수 있다. 이를 for문으로 접근하여 새로운 dict에 넣고 json으로 보낼 수 도 있지만 내장 함수를 이용했다. json.loads(serialize('json',profiles))
![image](https://user-images.githubusercontent.com/69501435/178146184-597bd61e-db3c-49a5-bbea-c35f5c78b2b3.png)

### read_one
```python
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
```
데이터가 있느냐 없으면 404뱉어내라는 get_object_or_404()함수, 그 데이터로 dict형으로 만들어 낸다. 이들은 class의 내부 변수로 접근할 수 있다. 그 내용 바탕으로 클라이언트로 조회한 데이터를 전송한다.

![image](https://user-images.githubusercontent.com/69501435/178146319-7e0d7588-b9be-4be4-9cfe-62f12111d7b8.png)

