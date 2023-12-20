#!/bin/bash

if [ "$DEBUG" == True ]; then
  python manage.py runserver 0.0.0.0:8000
else
  gunicorn --bind=0.0.0.0:8000 tree_menu_app.wsgi:application 
fi