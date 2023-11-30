# Social Network Analysis
[![Build Status](https://travis-ci.org/alexeykorevin/social_network_analysis.svg?branch=master)](https://travis-ci.org/alexeykorevin/social_network_analysis

a project that collects and analyzes information from social networks

## About project
the purpose of the project is a platform for collecting data such as posts, views, comments, followers, ... from social networks and keeping statistics.

In addition, it works as a platform for storing social data

## Social networks accepted by the platform:

* Telegram  ✅
* Instagram ✅
* Facebook  ✅
* Youtube   ✅
* Twitter   ✅
* Tiktok    ✅
* Web sites ✅ (with API)

## Installation
```bash'
pip3 install -r requirements.txt
```

## Make migrations and migrate
```bash
python3 manage.py makemigrations

python3 manage.py migrate
```


## Run project
```bash
python3 manage.py runserver 8000
```

## License
[MIT](https://choosealicense.com/licenses/mit/)