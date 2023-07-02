from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    picture = models.ImageField(upload_to="pictures/%Y/%m/%d", blank=True)
    author = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="author"
    )

    def __str__(self):
        return f"Picture -> [name={self.name}]"
