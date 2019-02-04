from django.db import models
from datetime import datetime


class Dash(models.Model):
    dash_title = models.CharField(max_length=200)
    dash_content = models.TextField()
    dash_published = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        return self.dash_title