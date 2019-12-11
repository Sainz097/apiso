from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField('Name',max_length=50)
    lastName = models.CharField('Lastname',max_length=50)
    age = models.IntegerField('Age',default=0)
    sex = models.CharField('Sex',max_length=25)
    address = models.TextField()
    collegeCareer = models.CharField('collegeCareer',max_length=50)

    def __str__(self):
        return '{0},{1}'.format(self.name,self.lastName,self.age,self.sex,self.address,self.collegeCareer)


# class collageCareer(models.Model):
#     name=models.CharField('Name',max_length=50)

