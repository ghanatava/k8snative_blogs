# blogs_corey

This is a simple blogging website built on django.

How to run:

Using DockerHub image:

$ docker pull ghanatava/blogs
$ docker run -it --name container_name -p 8000:8000 ghanatava/blogs

Building the image on local system:
navigate to the project directory

$ docker build . -t name for your image
$ docker run -it --name container_name -p 8000:8000 image name

Running on your local machine

$ git clone https://github.com/ghanatava/blogs_corey.git
$ python manage.py migrate
$ python manage.py runserver
