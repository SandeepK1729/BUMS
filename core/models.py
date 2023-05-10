from django.db import models

class Registration(models.Model):
    army_no         = models.IntegerField()
    rank            = models.IntegerField()
    name            = models.TextField()
    appointment     = models.TextField()
    sub_unit        = models.TextField()
    medical_cat     = models.TextField(verbose_name = "Medical Category")
    age             = models.IntegerField()

    def __str__(self):
        return self.name

