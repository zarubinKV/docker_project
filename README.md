# docker_project
Учебный проект

Есть три контейнера: БД MySQL, writer, reader. БД хранит данные, writer (localhost:8080) пишет в БД каждый раз, когда к нему обращаются, reader (localhost:8081) читает из бд кол-во обращений за сегодня и выводит при обращении.

***
## Быстрый старт
1) cd <project root directory>
2) docker build -t writer ./writer/
3) docker build -t reader ./reader/
4) docker-compose up
***
  
