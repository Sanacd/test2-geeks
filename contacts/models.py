from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField()
    message = models.TextField()

    
    def __str__(self):
        return self.name
