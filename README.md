# Personal-Blog
Personal Blog is a web application for that allows users to post and alter blogs as writers.
April 2019.

## By Shirley Keter
## Description
Personal-Blog is a web application where users can subscribe to the blog to get the latest updates on articles.The blog allows writers to create ,post and delete blogs.Users are able to view and comment on blogs.

## Set-up and Installation
Prerequiites
- Python 3.6
- Ubuntu software

#### Clone the Repo
Run the following command on the terminal: git clone https://github.com/chiriket/Personal-Blog.git && cd Personal-Blog

#### Install Postgres

#### Create a Virtual Environment
Run the following commands in the same terminal:

sudo apt-get install python3.6-venv
python3.6 -m venv virtual
source virtual/bin/activate
Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements

#### Prepare environment variables
* export DATABASE_URL='postgresql+psycopg2://<your-username>:<your-password>@localhost/personalblog'
* export SECRET_KEY='Your secret key'
* export DATABASE_URL_TEST='postgresql+psycopg2://<your-username>:<your-password>@localhost/personallog_test'
* export MAIL_USE_TLS=1
* export MAIL_USERNAME=<your-email>
* Run Database Migrations
* python manage.py db init
* python manage.py db migrate -m "initial migration"
* python manage.py db upgrade
* Running the app in development
In the same terminal type: python3 manage.py server

Open the browser on http://localhost:5000/

## Known bugs
There are no known bugs.

## Technologies used
- Python 3.6
- HTML
- Bootstrap 4
- JavaScript
- Heroku
- Postgresql

## Support and contact details
Contact me on shirleyketer@gmail.com.

## License
Copyright (c) Shirley Keter 
MIT 2019