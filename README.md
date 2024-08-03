# Website for CRUD Operations with ZNO Data.

A project realized to create an application in the form of a Website using Docker containers. 
It performs CRUD operations on the data in tables, which contain results of the ZNO (external examination in Ukraine).

#Інструкція

1) Add ZN0 data of 2019 and 2021 in the app folder.
   
Data source: https://zno.testportal.com.ua/stat

2) For running(creating containers) perform next command:

```bach
docker-compose create 
```
3) Run containers db-1, app-1 in that order.
4) Wait until app ends its work.
5) Run container flyway-1. Wait message "flyway exited with code 0".
6) Run container new_app-1. 
7) Go to localhost:5000
