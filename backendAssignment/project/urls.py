from django.contrib import admin
from django.urls import path,include
from posts.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",json_response),
    path('profiles/', include('profiles.urls'))
]