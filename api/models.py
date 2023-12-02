from django.db import models

class Programmer(models.Model):
    fullname  = models.CharField(max_length=50)
    nickname  = models.CharField(max_length=50)
    age       = models.IntegerField()
    language  = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nickname
