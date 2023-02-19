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

the comments help to conveythe lessons learned in talking through each instruction line



HOMEWORK
