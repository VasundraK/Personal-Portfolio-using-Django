# models.py

from django.db import models

class Project(models.Model):
    class Meta:
        db_table = 'personal_project'
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

