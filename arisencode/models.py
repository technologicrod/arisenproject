from django.db import models


class List(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    #primary_id = models.AutoField(primary_key=True, default = 0)

    def __int__(self):
        return self.id
