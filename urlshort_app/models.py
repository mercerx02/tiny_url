from django.db import models
from django.contrib.auth.models import User


class URL(models.Model):
    url_long = models.TextField(blank=True)
    url_short = models.TextField(blank=True)
    time_created = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)



