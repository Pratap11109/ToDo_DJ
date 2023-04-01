from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PRIORITY=(
    (1,"High"),
    (3,"Medium"),
    (3,"Low"),
    (4,"No Priority"),
)
class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date = models.DateTimeField(blank=True,null=True)
    priority = models.IntegerField(choices=PRIORITY)
    description = models.TextField(blank=True,null=True) 

    def __str__(self) -> str:
        return str(self.title)
