## Running application in docker containers:
#### Using Docker CLI
```
docker network ls
docker network create --driver bridge micro_network (skip if already created)
docker build -t file-manager-srv .
docker run -p 8001:8001 --detach --name file-manager-service --net=micro_network file-manager-srv
```