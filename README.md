# mbti-classifier-web-app

Task: Find if DigitalOcean offers domains to purchase  

Project Inspiration: [source](https://github.com/josephlee94/intuitive-deep-learning/blob/master/Building%20a%20Web%20Application%20to%20Deploy%20Machine%20Learning%C2%A0Models/imgrec_webapp.py)  

Activate the environment  
```
. .venv/bin/activate
```

Running Gunicorn(WSGI)  
```
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

## Inspiration
[Dockerizing Flask with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/)  
[Deploying a Flask To-Do App with Docker, Nginx, and MySQL](https://netopsautomation.medium.com/deploying-a-flask-to-do-app-with-docker-nginx-and-mysql-4b85a7e929a3)  
[Nginx: Setting Up a Simple Proxy Server Using Docker and Python/Django…](https://teke42.wordpress.com/2018/01/19/nginx-setting-up-a-simple-proxy-server-using-docker-and-python-django/)  
[How To Serve Flask Applications with Gunicorn and Nginx on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04)  
