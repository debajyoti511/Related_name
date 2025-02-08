from django.db import models

# Create your models here.
class School(models.Model):
    sname = models.CharField(max_length=50, primary_key=True)
    principal = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    loc = models.CharField(max_length=50)

    def __str__(self):
        return self.sname


class Student(models.Model):
    sid = models.IntegerField(primary_key=True)
    sname = models.ForeignKey(School, on_delete=models.CASCADE, related_name = 'students')
    stdname = models.CharField(max_length=50)
    pno = models.CharField(max_length=50)
    add = models.CharField(max_length=50)

    def __str__(self):
        return self.stdname
    