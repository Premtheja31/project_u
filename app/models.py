from django.db import models

# Create your models here.
class Student_marks(models.Model):
    name=models.CharField(max_length=100,null=False)
    gender=models.CharField(max_length=100,null=False)
    dob=models.DateField(null=False)
    maths=models.IntegerField(null=False)
    physics=models.IntegerField(null=False)
    chemistry=models.IntegerField(null=False)
    english=models.IntegerField(null=False)
    biology=models.IntegerField(null=False)
    economics=models.IntegerField(null=False)
    history=models.IntegerField(null=False)
    civics=models.IntegerField(null=False)
