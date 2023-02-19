# go out to docker hub and get a python container called 3.10-slim-buster
# you can go to docker hub and see that it's calliong to a debian docker file
# from scratch = official docker empty image
FROM python:3.10-slim-buster

# Inside Container
# make a new folder inside the container
# this is saying change the directory to /backend-flask in 
WORKDIR /backend-flask

# Outside -> Inside
# copying the reqruirements.txt into the current folder of the container
COPY requirements.txt requirements.txt

# Inside Container
# Install the python libraries used inside the app
# Run command is creating a "Layer" in the image
# run helps to build the image
RUN pip3 install -r requirements.txt

# Outside Conatiner -> Inside Container
# . means everything in the current directory
# first period . - /backend-flask (outside container)
# second period . /backend-flask (inside container)
COPY . .

# set environment variables (envars)
# these get set inside the container and will remain set while the container is running
ENV FLASK_ENV=development

EXPOSE ${PORT}

# CMD (Command)
# CMD is the command the container is going to run when it's starts up
# python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]