from django.db import models
class EmpModel(models.Model):
    id = models.IntegerField().primary_key="true"
    empname=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    occupation = models.CharField(max_length=150)
    empsal = models.IntegerField()
    gender = models.CharField(max_length=1)
    address =models.CharField(max_length=150)
    class Meta:
        db_table="employee"




