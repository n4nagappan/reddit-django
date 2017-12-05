# reddit-django

### Setup using docker

1. Clone the repo
```
# clone repo
git clone https://github.com/n4nagappan/reddit-django.git
```

2. Setup secret keys
```
# setup secret keys
cd reddit-django/counter/counter/
cp settings_secret_template.py settings_secret.py
```

Make sure you replace the placeholders with your secret keys

3. Build docker images
```
# navigate to project root
cd ../../
pwd
# <some-path>/reddit-django

docker-compose build
```

4. Start the containers
```
docker-compose up
```

### Setup without docker
1. Clone the repo
```
# clone repo
git clone https://github.com/n4nagappan/reddit-django.git
```

2. Setup env
```
# Make sure you are on python3 and venv installed
cd reddit-django
venv reddit-env
source reddit-env/bin/activate
python --version
# Python 3.5.2
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Setup secret keys
```
# setup secret keys
cd counter/counter/
cp settings_secret_template.py settings_secret.py
```

Make sure you replace the placeholders with your secret keys   

5. Start server
```
cd ..
pwd
# <some-path>/reddit-django/counter

# start server
python manage.py runserver
```

### Sample requests
1. Fetch counter stats for a given subreddit
```
http localhost:8000/subreddits/facepalm
```
2. Fetch counter stats for a given subreddit with a limit query parameter for the number of posts to fetch. Default value of limit is ```100```

```
http localhost:8000/subreddits/facepalm?limit=2
```

  Sample response:
```
{
    "description_count": 87,
    "display_name": "facepalm",
    "display_name_count": 1,
    "posts": [
        {
            "comments_info": "http://localhost:8000/subreddits/facepalm/5plzx7/comments_info",
            "id": "5plzx7",
            "id_count": 1,
            "title": "New rule regarding minors on this sub.",
            "title_count": 0,
            "url": "https://www.reddit.com/r/facepalm/comments/5plzx7/new_rule_regarding_minors_on_this_sub/",
            "url_count": 3
        },
        {
            "comments_info": "http://localhost:8000/subreddits/facepalm/76nbmm/comments_info",
            "id": "76nbmm",
            "id_count": 0,
            "title": "Remember to COMPLETELY BLACK OUT ALL PERSONAL INFORMATION! This includes real names, profile pictures, usernames, or anything else along those lines.",
            "title_count": 4,
            "url": "https://www.reddit.com/r/facepalm/comments/76nbmm/remember_to_completely_black_out_all_personal/",
            "url_count": 4
        }
    ],
    "title": "A gallery of inexplicable stupidity",
    "title_count": 2
}
```

2. Fetch counter stats for comments under a given post of a subreddit
```
http http://localhost:8000/subreddits/facepalm/5plzx7/comments_info
```
  You can get this link from the first subreddit request in the ```comments_info field```.

  Sample response :
```
{
    "comments_link": "https://www.reddit.com/r/facepalm/comments/5plzx7",
    "post_id": "5plzx7",
    "total_count": 87
}
```

