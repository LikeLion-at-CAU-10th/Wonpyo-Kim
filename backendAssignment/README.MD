1. [week1](#1-week1)
2. [week2](#2-week2)
3. [week3](#3-week3)
## 1. week1

![2022-06-27 (7)](https://user-images.githubusercontent.com/69501435/175920511-c94d1990-12df-4c39-ba7e-db89bafded26.png)

1. 가상환경 설정하기 (python -m venv ~)
2. 가상환경 실행시키기 ( ~/Scripts/activate)
3. 장고 설치 (pip install django)
4. django-admin startproject ~ .
5. django-admin startapp ~
6. settings.py에서 secretkey, installedapps 설정하기
7. views 연결 및 urls에 path연결

## 2. week2

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

### remove
```python
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
```
post의 요청으로 그 데이터를 우선 찾는다. 그 후 삭제할 데이터를 클라에게 보내주기 위해 data (dict 형)으로 저장해두고 delete로 삭제한다. 

![image](https://user-images.githubusercontent.com/69501435/178146608-69c429e4-3c69-41ba-bcc5-5584b69916c3.png)

### update
```python
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
```

아직 좋은 방법이 무엇인지 잘 모르겠다. 그 remove까지 똑같이 진행하고 실제 그 id로 새로 데이터를 create하는 방식으로 코드를 작성했다. update를 한번에 하는 방법이 있을거 같은데 그것은 나중에 배워보고 수정해보겠다.

![image](https://user-images.githubusercontent.com/69501435/178146748-2040485f-3331-4d69-9b2d-a82aced79fa2.png)

## 3. week3
### admin 설정
python manage.py createsuperuser -> admin.py 에 들어가서 admin.site.register(모델명)

### forien_key 설정
우선 나만의 모델링의 작업이 필요했다. profile에 저장된 한사람 기준으로 자신이 기록해두고 싶은 url을 넣을 수 있도록 url 모델을 새로 정의 해봤다.
models.py 에 다음과 같은 모델링을 추가해보도록 하자.
```python
class Url(models.Model):
    profile_name = models.ForeignKey("Profile", on_delete = models.CASCADE, null = True, blank = True)
    url_name = models.CharField(max_length = 100, null = True, blank = True)
    url = models.URLField(max_length = 100)
```
즉 Profile의 pk가 Url 의 외래키 참조 대상이고 그 정보는 profile_name에 저장해놓았다.
1. python manage.py makemigrations
2. pyhton manage.py migrate 로 합치기!

### create_profile_url
```python 
def create_profile_url(request, id):
    if request.method == "POST":
        profile_url = get_object_or_404(Profile, pk = id)
        data = json.loads(request.body)
        new_url = Url.objects.create(
            profile_name = profile_url,
            url_name = data['url_name'],
            url = data['url']
        )
        
        url_info = {
            "id" : new_url.id,
            "url_name" : new_url.url_name,
            "url" : new_url.url
        }
        
        return JsonResponse({
            "status" : 200,
            "success" : True,
            "message" : "생성 성공!",
            "data" : url_info
        })
    return JsonResponse({
        "status" : 200,
        "success" : False,
        "message" : "POST 요청으로 데이터랑 보내주세요!",
        "data" : None
    }) 
```
1. 우선 Profile의 외래키이므로 Profile의 pk가 있는 값인지 확인 해야한다.
```python
profile_url = get_object_or_404(Profile, pk = id)
```
2. data는 body에 json 형태로 들어오므로 그 값을 load
```python
data = json.loads(request.body)
```
3. 그 후 과정은 Profile의 create 과정이랑 동일
![image](https://user-images.githubusercontent.com/69501435/179153480-8bd3f757-ff58-4d9c-94ec-e99501d4963e.png)
Profile의 pk가 5인 친구의 Url을 만드는 과정...
![image](https://user-images.githubusercontent.com/69501435/179153568-a7ce9e45-873d-4dca-a4ca-63f0b07b24c8.png)
admin페이지 내부에서 Profile_name(Url model 에서 foreign key로 지정해둔 변수)를 보면 Profile object(5) ---- > Profile의 pk가 5인친구를 foriegn key로 받아왔다는 뜻인것 같다.
![image](https://user-images.githubusercontent.com/69501435/179153756-f3af7dc8-200f-4fd8-a0e0-3991cdae7602.png)
수정삭제등을 하기위해 하나더 생성해봤다.!!!

