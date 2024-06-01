from django.db import models


class Hello(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    class Meta:
        db_table = 'hello'
