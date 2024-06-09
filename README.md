# kb_fit

## Welcome to Kettlebell Fit

An app for documenting your kettlebell specific training sessions to keep track of your programs and progress. You can view the exercises that have been added by users witout logging in, but will need to create an account to log sessions and add info.
The app uses many of Django's quick and easy built in features, authentication and authorization included.
This is my first attempt at an application in Python and Django, so please be kind!

## Getting started

- Start up your Python Virtual Environment
  `source django_env/bin/activate`
- Start up the app
  `python manage.py runserver`

## [Visit deployed app here](https://kettlebell-fit-1513cd41f148.herokuapp.com/)

## Technology Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

- Styled with [Bootswatch](https://bootswatch.com/)

- <a target="_blank" href="https://icons8.com/icon/ur7Wlis7nVHs/kettlebell">Kettlebell</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>

## Requirements

```
asgiref==3.8.1
boto3==1.34.91
botocore==1.34.91
certifi==2024.2.2
charset-normalizer==3.3.2
dj-database-url==2.1.0
Django==4.2.11
django-environ==0.11.2
django-on-heroku==1.1.2
django-widget-tweaks==1.5.0
gunicorn==22.0.0
idna==3.7
jmespath==1.0.1
packaging==24.0
pillow==10.3.0
psycopg2==2.9.9
psycopg2-binary==2.9.9
python-dateutil==2.9.0.post0
requests==2.31.0
s3transfer==0.10.1
six==1.16.0
sqlparse==0.5.0
typing_extensions==4.11.0
urllib3==1.26.18
whitenoise==6.6.0
```

### Upcoming Features

- More exercise detail (muscles worked, form tips, etc)
- Search for exercises by type
- Full-site searchability
- Data comparison
- Home page background animations
