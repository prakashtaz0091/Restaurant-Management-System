from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=20)
    is_reserved = models.BooleanField(default=False, null=True)
    
    def __str__(self):
        return self.name