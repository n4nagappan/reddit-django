from django.db import models

# Create your models here.
# Create your models here.
class Subreddit(models.Model):
    display_name = models.CharField(max_length=30)
    display_name_count = models.IntegerField()
    title_count = models.IntegerField()
    description_count = models.IntegerField()
