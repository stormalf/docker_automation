#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author : stormalf  stormalf.summonerswar@gmail.com
# sample docker test sdk example with python 

import docker

#create a file with content log for each container_id
def output_log(container):
  filename = "docker_" + container.id
  fichier = open(filename, "wb")
  fichier.write(container.logs())
  fichier.close()


#the docker daemon should be running 
client = docker.from_env()
#download if necessary and run a container from alpine:latest image a hello world and exit
print(client.containers.run("alpine:latest", ["echo", "hello", "world"]))
# run a container in background  
container = client.containers.run("alpine:latest", detach=True)
print(container.id)
#list all containers and for each of them retrieve the container log and write in a file docker_${container_id}
for container in client.containers.list():
  print(container.id)
  output_log(container)

#display all id images
for image in client.images.list():
  print(image.id)











