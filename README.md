# Personal-Blog
Personal Blog is a web application for c
2019

## By Shirley Keter
#### Description
Personal-Blog is a web application where users can subscribe to the blog to get the latest updates on articles.The blog allows writers to create , post and delete blogs.Users can are able to view and comment on blogs.

## Set-up and Installation
Prerequiites
- Python 3.6
- Ubuntu software

## Clone the Repo
Run the following command on the terminal: git clone https://github.com/chiriket/Personal-Blog.git && cd Personal-Blog

## Install Postgres

## Create a Virtual Environment
Run the following commands in the same terminal:

sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements

## Prepare environment variables
export DATABASE_URL='postgresql+psycopg2://<your-username>:<your-password>@localhost/carblog'
export SECRET_KEY='Your secret key'
export DATABASE_URL_TEST='postgresql+psycopg2://<your-username>:<your-password>@localhost/carblog_test'
export MAIL_SERVER='smtp.googlemail.com'
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-email>
export MAIL_PASSWORD=<your-password> 
Run Database Migrations
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
Running the app in development
In the same terminal type: python3 manage.py server

Open the browser on http://localhost:5000/

## Known bugs
Sending batch emails bug If others are found, drop me a message

## Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- JavaScript
- Heroku
- Postgresql

## Support and contact details
Contact me on developer.waweru@gmail.com for any comments, reviews or advice.

## License
Copyright (c) Shirley Keter 
MIT 2019