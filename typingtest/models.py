from django.db import models


class Words(models.Model):
    title = models.CharField(max_length=50, default='test')
    text = models.TextField()

    def __str__(self):
        return self.title
