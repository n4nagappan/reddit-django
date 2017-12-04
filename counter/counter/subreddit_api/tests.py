from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

# Create your tests here.

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()
        self.client = APIClient()

    def test_subreddit_analysis(self):
        response = self.client.get('/subreddits/facepalm')
        self.assertEqual( response.status_code, 200 )
        self.assertEqual( response.data["display_name"]  , "facepalm" )
        self.assertEqual( response.data["title"] , "A gallery of inexplicable stupidity" )
        self.assertEqual( response.data["title_count"] , 2 )

    def test_comments_info_analysis(self):
        response = self.client.get('/subreddits/facepalm/7gwomt/comments_info')
        self.assertEqual( response.status_code, 200 )
        self.assertEqual( response.data["post_id"]  , "7gwomt" )
        self.assertEqual( response.data["comments_link"] , "https://www.reddit.com/r/facepalm/comments/7gwomt" )
        self.assertEqual( response.data["total_count"] , 52 )
