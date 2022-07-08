from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length = 40, default = "김원표", null = True, blank = True)
    age = models.IntegerField(default = 20, null = True, blank = True)
    phone = models.CharField(max_length=50, default= "none", null = True, blank = True)
