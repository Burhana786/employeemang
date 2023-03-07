from django.db import models

# Create your models here.

class RegModel(models.Model):
    eid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    experiance=models.IntegerField()

    def __str__(self):
        return self.name




class Person(models.Model):
    firstname=models.CharField(max_length=100)
    secondname=models.CharField(max_length=100)


class Department(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_no=models.IntegerField()
    dept_description=models.CharField(max_length=100)

    

class Manager(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    pic=models.ImageField(upload_to='profilepic',null=True)