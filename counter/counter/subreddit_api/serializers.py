from counter.subreddit_api.models import Subreddit, Post, CommentsInfo
from rest_framework import serializers

class CommentsInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommentsInfo
        fields = ( 'post_id', 'total_count' , 'comments_link' )

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ( 'id', 'title', 'url' , 'id_count' , 'title_count' , 'url_count' , 'comments_info' )

class SubredditSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = Subreddit
        fields = ( 'display_name', 'title', 'display_name_count' , 'title_count', 'description_count' , 'posts' )

    def create(self, validated_data):
        posts_data = validated_data.pop('posts')
        subreddit = Subreddit.objects.create(**validated_data)
        for post_data in posts_data:
            Post.objects.create(subreddit=subreddit, **post_data)
        return subreddit
