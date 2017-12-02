from counter.subreddit_api.models import Subreddit
from rest_framework import serializers

class SubredditSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subreddit
        fields = ( 'display_name', 'title', 'display_name_count' , 'title_count', 'description_count' )

