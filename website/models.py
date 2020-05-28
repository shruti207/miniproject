from django.db import models

# Create your models here.
class TodoList(models.Model):

    
    content = models.TextField()
    completed = models.BooleanField(default=False)
    

