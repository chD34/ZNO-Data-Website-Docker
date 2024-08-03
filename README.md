
A project realized to create an application in the form of a Website using Docker containers. 
It performs CRUD operations on the data in tables, which contain results of the ZNO (external examination in Ukraine).

#Інструкція

1) For running(creating containers) perform next command:

```bach
docker-compose create 
```
2) Run containers db-1, app-1 in that order.
3) Wait until app ends its work.
4) Run container flyway-1. Wait message "flyway exited with code 0".
5) Run container new_app-1. 
6) Go to localhost:5000
