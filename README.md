## Api in Django

![CI](https://github.com/matheusfrancisco/django-api-trip-bike/workflows/CI/badge.svg?branch=master)

Install, make setup will enable pre-commit and lint,
always before commit will run test and lint.
```
pip install -r requirements-dev.txt
make setup
```

## Run test
test will run using sqlite
```
python manage.py test
```

## Run this simple API

```bash
docker-compose up -d
python manage.py migrate
```

Create a user
```bash
python manage.py createsuperuser
```


Get a Token Request:

```bash
curl -X POST \
  http://localhost:8000/api/v1/auth/login/ \
  -H 'content-type: application/json' \
  -d '{
    	"username": "new_user",
    	"password": "new_pass"
      }'
```

Response:
```
{
    token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Im5ld191c2VyIiwiZXhwIjoxNTQwNDkyMTQ2LCJlbWFpbCI6Im5ld191c2VyQG1haWwuY29tIn0.8_8S-5MYY-gXkkJ-emT97s-aW8JhMEGnOyahS20uPtQ"
}
```

List Trips to user auth
```bash
curl -X GET \
        http://localhost:8000/api/v1/trip/list/ \
     -H 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTk4MTQyOTUwLCJlbWFpbCI6ImFkbWluQGdtYWlsLmNvbSJ9.1lLzDf5k4LUIDE1QNkAUw9IbSBCE-h45QFgtW8A8ltk
```

Response:
```
[{"id":1,"start_date":"2020-08-20T11:20:29Z","end_date":"2020-08-20T13:21:33Z","classification":1,"rate":1}]
```

Update an trip, change the classification or rate:

```bash
curl -X PUT \
  http://localhost:8000/api/v1/trip/details/1/ \
  -H 'authorization: Bearer  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTk4MTQzMzc1LCJlbWFpbCI6ImFkbWluQGdtYWlsLmNvbSJ9.NtLBMZM87maBabARDF4dZx3pV4P0lOwX-GB1gfVjovY' \                 
  -H 'content-type: application/json' \
  -d '{
        "rate": 1,
        "classification": 3
      }'

```

Response:
```
{"id":1,"start_date":"2020-08-20T11:20:29Z","end_date":"2020-08-20T13:21:33Z","classification":3,"rate":1}%
```


Change only the classification:
```bash
curl -X PUT \
  http://localhost:8000/api/v1/trip/details/1/ \
  -H 'authorization: Bearer  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTk4MTQzMzc1LCJlbWFpbCI6ImFkbWluQGdtYWlsLmNvbSJ9.NtLBMZM87maBabARDF4dZx3pV4P0lOwX-GB1gfVjovY' \                 
  -H 'content-type: application/json' \
  -d '{
        "classification": 2
      }'
```

Response:
```
{"id":1,"start_date":"2020-08-20T11:20:29Z","end_date":"2020-08-20T13:21:33Z","classification":2,"rate":1}% 
```


## TODO
- [x] Add pagination to return 100 trips per page on api/v1/trip/list
- [ ] Add celery to background tasks
- [ ] Try to move business logic to domain layer
