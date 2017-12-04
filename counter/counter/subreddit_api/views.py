from collections import OrderedDict
from django.shortcuts import render
from django.http import Http404
from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from counter.subreddit_api.models import Subreddit, CommentsInfo
from counter.subreddit_api.serializers import SubredditSerializer, CommentsInfoSerializer
from counter.subreddit_api.subreddit_analyze import analyze_subreddit, analyze_comments

CACHE_EXPIRY_TIME = 100


# Create your views here.
class SubredditAnalysisDetailedView(APIView):
    """
    Analysis report for a given subreddit
    """
    def get(self, request, name, format=None):
        print("Analyzing subreddit : ", name)

        full_url = request.build_absolute_uri('?')
        params = get_params( request )

        # check cache first
        subreddit = cache.get( get_subreddit_key(name, params) )

        if subreddit is None:
            subreddit = analyze_subreddit( name, full_url , params)
            print( "fetched from reddit" )
            # print( subreddit )
            serializer = SubredditSerializer(data=subreddit)
            if serializer.is_valid():
                # serializer.save()
                cache.set( get_subreddit_key( name , params ), serializer.data, CACHE_EXPIRY_TIME)
                return Response(serializer.data)
            
        else:
            print( "found in cache" )
            # print( subreddit )
            serializer = SubredditSerializer(subreddit)
            return Response(serializer.data)

                            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentsInfoView(APIView):
    """
    Analysis report for comments on a subreddit post
    """
    def get(self, request, name, post_id, format=None):
        print("Analyzing Comments info for subreddit : ", name, "; Post Id : ", post_id)
        comments_info = cache.get( get_comments_info_key(name, post_id) )

        if comments_info is None:
            comments_info = analyze_comments(post_id)
            print( "fetched from reddit" )
            # print( comments_info )
            serializer = CommentsInfoSerializer(data=comments_info)
            if serializer.is_valid():
                # serializer.save()
                cache.set( get_comments_info_key(name, post_id) , serializer.data, CACHE_EXPIRY_TIME)
                return Response(serializer.data)
            
        else:
            print( "found in cache" )
            # print( comments_info )
            serializer = CommentsInfoSerializer(comments_info)
            return Response(serializer.data)

                            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DefaultView(APIView):
    """
    Default View
    """
    def get(self, request, format=None):
        return Response({ "message" : "Subreddit counter api v0.1"})

def get_params(request):
    params = OrderedDict({})

    limit = request.GET.get('limit')
    params[ "limit" ] = int(limit) if limit is not None and limit.isdigit() else 100

    return params

def get_comments_info_key(name, post_id):
    return "comments_info_" + name + "_" + post_id

def get_subreddit_key(name, params):
    key = "subreddit_" + name + "_" + str( params )
    return key
