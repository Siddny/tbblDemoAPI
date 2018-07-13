Getting Started
These instructions will get you started running this demo.

Prerequisites
Django 1.11
python3
Installation
Clone this repo.

Create a new virtual environment for this application and activate it. 

virtualenv -p python3 env
source env/bin/activate

After activating the virtual environment, point to the root folder of this project and run:

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

