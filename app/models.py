from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(null=True, blank=True, max_length=300)
    first_name = models.CharField(default="", null=False)
    content = models.TextField(null=False)
    modified_date = models.DateTimeField(auto_now=True)

