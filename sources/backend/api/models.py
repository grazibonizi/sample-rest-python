from django.db import models


# Create your models here.
class Todo(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	date = models.DateTimeField()
	isComplete = models.BooleanField()
