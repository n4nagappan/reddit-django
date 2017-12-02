from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from counter.subreddit_api.models import Subreddit
from counter.subreddit_api.serializers import SubredditSerializer
from counter.subreddit_api.subreddit_analyze import analyze

# Create your views here.
class SubredditAnalysisDetailedView(APIView):
    """
    Analysis report for a given subreddit
    """
    def get(self, request, name, format=None):
        print("Analyzing ", name)
        subreddit = Subreddit.objects.filter(display_name=name).first()
        if subreddit is None:
            subreddit = analyze(name)
            print( subreddit )
        serializer = SubredditSerializer(subreddit)
        return Response(serializer.data)

