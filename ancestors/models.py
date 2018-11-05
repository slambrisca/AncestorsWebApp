from django.db import models
from ancestors.utils import *

class File(models.Model):
    path = models.CharField(max_length=100)
    person = models.ForeignKey("Person",on_delete=models.CASCADE)

    def getPerson(self):
        return self.person

    def getPath(self):
        return self.path

    def __str__(self):
        return self.path

class Person(models.Model):

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=Gender.CHOICES, default=Gender.NONE)

    id_type = models.CharField(max_length=3,choices=IdType.CHOICES)
    id_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name +" "+ self.surname + " " + self.id_type + ":"  + self.id_number

    def getFiles(self):
        return list(self.file_set.all())

    def addFile(self,filePath):
        return self.file_set.create(path=filePath)


