from random import choice
from django.db import models

class Images(models.Model):
    alt = models.CharField(max_length=60)
    link = models.CharField(max_length=400, default=None, blank=True, null=True)
    image = models.ImageField(upload_to="",  default=None, blank=True, null=True)
    order = models.IntegerField(default=0)

    page_names = [
        ('HO', 'Home'),
        ('PO', 'Portfolio'),
    ]
    location = models.CharField(max_length=60, choices=page_names, default='HO')
    

    def __str__(self):
        return self.alt
