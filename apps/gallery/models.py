from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):

    ORIENTATIONS = [
        ("VERTICAL", "Vertical"),
        ("HORIZONTAL", "Horizontal"),
        ("SQUARE", "Quadrada"),
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    picture = models.ImageField(upload_to="pictures/%Y/%m/%d", blank=True)
    orientation = models.CharField(max_length=100, choices=ORIENTATIONS, default='')
    author = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="author"
    )

    def __str__(self):
        return f"Picture -> [name={self.name}]"
