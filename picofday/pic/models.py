from django.db import models

class Img(models.Model):
    upload = models.TextField()
    title = models.CharField(max_length=200)
    expln = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.upload
