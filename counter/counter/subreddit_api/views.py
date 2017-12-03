from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from counter.subreddit_api.models import Subreddit, CommentsInfo
from counter.subreddit_api.serializers import SubredditSerializer, CommentsInfoSerializer
from counter.subreddit_api.subreddit_analyze import analyze, analyze_comments

# Create your views here.
class SubredditAnalysisDetailedView(APIView):
    """
    Analysis report for a given subreddit
    """
    def get(self, request, name, format=None):
        print("Analyzing ", name)
        subreddit = Subreddit.objects.filter(display_name=name).first()
        full_url = request.build_absolute_uri()
        if subreddit is None:
            subreddit = analyze( name, full_url )
            print( "fetched from reddit" )
            print( subreddit )
            serializer = SubredditSerializer(data=subreddit)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            
        else:
            print( "found in db" )
            print( subreddit )
            serializer = SubredditSerializer(subreddit)
            return Response(serializer.data)

                            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentsInfoView(APIView):
    """
    Analysis report for a given subreddit
    """
    def get(self, request, name, post_id, format=None):
        print("Analyzing Comments info for subreddit : ", name, "; Post Id : ", post_id)
        comments_info = CommentsInfo.objects.filter(post_id=post_id).first()
        if comments_info is None:
            comments_info = analyze_comments(post_id)
            print( "fetched from reddit" )
            print( comments_info )
            serializer = CommentsInfoSerializer(data=comments_info)
            if serializer.is_valid():
                print( serializer.validated_data )
                serializer.save()
                return Response(serializer.data)
            
        else:
            print( "found in db" )
            print( comments_info )
            serializer = CommentsInfoSerializer(comments_info)
            return Response(serializer.data)

                            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
