from django.db import models

# Create your models here.

# The list holding specific user's to-do items
class List(models.Model):
    pass

# The to-do item itself
class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        default=None)


