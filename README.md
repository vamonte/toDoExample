# toDoExample

toDoExample is a DjangoRestFramework project used for some personal examples.


### How to

To run the stack you just have to use the docker-compose file.

```shell
docker-compose up 
```
The project provides one HTTP resource named 'todos'.
You may request it as bellow.

```shell
#List all the todos
curl http://localhost:8000/todos/

#Add one todo
curl -X POST -H "content-type: application/json" -d '{"title": "test"}' http://localhost:8000/todos/

#Retrieve one todo
curl http://localhost:8000/todos/<id>/

#Update one todo
curl -X PUT -H "content-type: application/json" -d '{"title": "new title"}' http://localhost:8000/todos/1/
 
#Delete one todo
curl -X DELETE http://localhost:8000/todos/1/
```

You may download the container image to reuse the app for your own examples.

```shell
docker pull vmonte/todoexample:latest
```
