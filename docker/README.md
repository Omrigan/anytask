# Deploying anytask through docker

```
cd docker/
./build-image.sh
cp docker-compose-example.yml docker-compose.yml
docker-compose -up
docker-compose exec web /app/anytask/manage.py createsuperuser
```

Anytask will become avalible at `localhost:80`

Database will be stored in `docker/data/`
