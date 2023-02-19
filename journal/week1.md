# Week 1 — App Containerization

LIVE STREAM

tech topics covered
node vs python
mpm?npn?

Benefits and use cases
----------------------
Containerization makes it more portables and gets you closer to the deployment environement

You can easily kill full env and restart if issues encountered

ex. Different versions of python, other languages, variants of OS's: simplifies down to 1 configuration

get the docker file in there so that it is consistent across developers to testers, etc.


Resources 

dockerhub : container registry provided by docker where you can host your own container images, you can build and push image to a container registry, someone to consume would pull from the registry (github for docker images)

linuxserver.io : provide docker files that are well documented, following best practices

jfrog : artifact repository (like artifactory?)

Instruction Overview


write a couple docker files

get them running

publish to dockerhub

Working Notes

created a docker file

each line o fthe docker file is an instruction for the system

i added comments in the docker file using'#'

the comments help to convey the lessons learned in talking through each instruction line

we are using python version 3

we are using the flask framework which is web application framework

# This is the command that built the conatiner image using the series of instructions laid out in ./backend-flask/Dockerfile
docker build -t backend-flask ./backend-flask
docker build = command
-t  = tag/naming set to backend-flask
./backend-flask = looks for "Dockerfile" in here

docker build -t backend-flask ./backend-flask
should be ->
docker build -t backend-flask:1.0.0 ./backend-flask
to add tag "1.0.0"

docker images will list all of the docker images on the machine

when container is running

npm install

docker compose orchestrates multiple containers working together


HOMEWORK
