from django.db import models

class student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    mobile=models.CharField(max_length=15)

    def __str__(self):
        return self.name