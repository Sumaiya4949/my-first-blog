from django.db import models

# Create your models here.
class Teachers(models.Model):
    t_id=models.IntegerField()
    code=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=50)
    department=models.CharField(max_length=50)


    def __str__(self):
        return (self.name)
