from django.db import models

# class User(models.Model):
#     login = models.CharField(max_length=30)
#     password = models.CharField(max_length=50)
#     avatar = models.CharField(max_length=150)
#     reg_date = models.DateTimeField('date registrated')

#     def __unicode__(self):
#         return self.login

from django.contrib.auth.models import User

class GameUser(models.Model):
    user = models.OneToOneField(User)
    avatar = models.CharField(max_length=150)

    REQUIRED_FIELDS = ['avatar']
