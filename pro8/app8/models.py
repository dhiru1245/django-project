from django.db import models



class ContactData(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    mobile = models.BigIntegerField()


