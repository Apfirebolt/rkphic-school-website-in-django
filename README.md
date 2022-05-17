![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

# Website for a school - RKPHIC Nagal, Saharanpur ⚡️

## Project Briefing

A simple website for a school called Ram Krishna Paramhans Inter College situated in Nagal, Saharanpur, UP, India.

This website allows admin of the site to dynamically add notifications, schools, gallery images for this school. This website is created using Django - a popular web framework in Python which allows rapid development of features with a built in admin panel which was essential for this use case. The website uses Postgresql for database which makes it quite flexible with the scope of adding/removing fields in the database and create models for catering future requirements.
For the time being this web app can be found at https://rkphic.herokuapp.com/

Made with ❤️ by **[@apfirebolt](https://github.com/Apfirebolt/)**

Please find me [here](https://apgiiit.com/)
## Features

- Displays static and dynamic data through Django Jinja templates in a multi-page application written in Django.
- Has a built in admin panel through which admin can manipulate data of the website smoothly.
- Models are created for students, notifications and gallery. More models can easily be created as per future requirements.
- Hosted on Heroku through pipeline for smooth deployment when ever something is pushed on master branch,
- AWS S3 buckets can be easily configured to store static and media files.

## Built With

* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Bootstrap](https://getbootstrap.com/)
* [Postgres](https://www.postgresql.org/)
* [Heroku](https://dashboard.heroku.com/)

## Project setup

The project is created like a conventional Python and Django project. A virtual environment is created and all the relevant packages
are installed through reading 'requirements.txt' file. Multiple environments are setup
with different settings. Environment variables are directly read from Heroku for prod environment.

Procfile defines script to run on heroku server when the app starts or a
new deployment is completed.

```
web: python manage.py collectstatic --no-input; gunicorn rkphic_school.wsgi --log-file - --log-level debug

```

This serves the Django app through gunicorn server after collecting the static
files.

Runtime.txt file was included to specify the version of Python to be used
while installing packages.

## Issues

None so far, but heroku free tier database keeps on changing credentials. More would be added as they are discovered.

## Future Updates

- Expect UI improvements in near future for this app using Bootstrap as per feedback.
- New functionalities might be added in terms of changing models and views.

## Project Screenshots

Would be added later
