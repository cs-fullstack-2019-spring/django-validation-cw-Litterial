from django.db import models

# Create your models here.

class Car(models.Model):
    make=models.CharField(max_length=60)
    model=models.CharField(max_length=60)
    year = models.IntegerField(default=0)
    mph = models.IntegerField(default=0)


    def __str__(self):
        return self.make

