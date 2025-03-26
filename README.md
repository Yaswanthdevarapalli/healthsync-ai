HealthSync is a full-stack web application designed to monitor and analyze health data, such as heart rate and sleep hours, to assess health risks. 
The backend, built with Django and Django REST Framework, provides a RESTful API to store and retrieve health data, which is deployed on an AWS EC2 instance using Gunicorn for production-grade performance. 
The frontend, developed with React, fetches data from the API and displays it in a user-friendly table, allowing users to view health metrics and risk levels at a glance. 
This project integrates CORS for secure cross-origin requests and uses SQLite for data storage during development.
