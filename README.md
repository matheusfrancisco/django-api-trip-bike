## Api in Django

## Run this simple API

```bash
docker-compose up -d
python manage.py migrate
```


Get a Token Request:

```
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
