# About
##This project is a solution to a test provided by Jellyworkz. 
Part 1:
>Write a python script that will do the following:
Part 1:
We have an API server that returns a json response for the url with 100 values ( 1-100): https://jsonplaceholder.typicode.com/todos/{id}
For each id between 1-100 get the “userId” and “completed” fields.
If the status “completed” is “true” insert the “title” and “userId” into MySQL table “stories”


Part 2:
>Create Flask application with the following routes:
http://localhost:5000/user/{userId} This will print json of all stories related to userId
http://localhost:5000/story/{id} This will print json of specific story id.
http://localhost:5000/title/{title}
This will return all titles containing the data in the title.


## Technology stack
1. Interpreter - Python 3.6+
2. Web framework - Flask
3. Database	- MySQL
4. Web server - Ngnix
5. ORM - SqlAlchemy
6. Migrations framework - Alembic
7. Environments hosted by - docker with docker-compose
6. Project configuration - through environment variables

## What is needed to start the application
Docker and docker-compose installed.

## Installation
The installation process described below is considering that you are using Ubuntu
1. Navigate to `/your/installation/path/flaskProject/server`
2. Run `sudo docker-compose up -d --build`
3. Run `sudo docker exec -it app /opt/app/env/bin/alembic upgrade head`
#### Notes
In order to launch "Part 1" script you need to run:

`sudo docker exec -it app /opt/app/env/bin/python /opt/app/env/bin/task_1.py`
