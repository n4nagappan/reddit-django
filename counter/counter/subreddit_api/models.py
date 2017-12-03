from django.db import models

# Create your models here.
class Subreddit(models.Model):
    display_name = models.CharField(max_length=30)
    title = models.CharField(max_length=600)

    display_name_count = models.IntegerField()
    title_count = models.IntegerField()
    description_count = models.IntegerField()

class Post(models.Model):
    subreddit = models.ForeignKey(Subreddit, related_name='posts', on_delete=models.CASCADE)
    
    id = models.CharField( max_length=30, primary_key=True )
    title = models.CharField(max_length=600)
    url = models.CharField(max_length=600)
    id_count = models.IntegerField( )
    title_count = models.IntegerField()
    url_count = models.IntegerField()
