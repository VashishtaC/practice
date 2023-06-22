from django.db import models
class circle(models.Model):
    cname=models.CharField(max_length=30)
    cquantity=models.IntegerField()
    price=models.FloatField()
    class Meta:
        db_table="circle"
# Create your models here.
