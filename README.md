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

2. Fetch counter stats for comments under a given post of a subreddit
```
http http://localhost:8000/subreddits/facepalm/7h1lbq/comments_info
```
You can get this link from the first subreddit request 

3. Fetch counter stats for a given subreddit with a limit query parameter for the number of posts to fetch
```
http localhost:8000/subreddits/facepalm?limit=300
```
