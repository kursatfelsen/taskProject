# taskProject


## Install

    pip install -r requirements.txt

## Run the app

    python manage.py runserver


# REST API


## Get list of Things

### Request

`GET tasks/api`

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    []


## Get a task

### Request

`GET /tasks/api/id`

### Response

HTTP 200 OK
Allow: GET, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "title": "BBB",
    "is_completed": false,
    "created_at": "2022-09-08T20:50:31.811935Z",
    "last_updated": "2022-09-08T21:02:13.466054Z",
    "is_active": true
}


## Get a non-existing task

### Request

`GET tasks/api/1`

### Response

HTTP 400 Bad Request
Allow: GET, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "response": "Object with task id does not exists"
}


## Update task

### Request

PUT /tasks/api/7/

### Response


HTTP 200 OK
Allow: GET, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "title": "BBB",
    "is_completed": false,
    "created_at": "2022-09-08T20:50:31.811935Z",
    "last_updated": "2022-09-08T21:02:13.466054Z",
    "is_active": true
}


## Create a new task

### Request

PUT /tasks/api/

### Response

HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "title": "CCC",
    "is_completed": false,
    "created_at": "2022-09-08T21:05:53.773985Z",
    "last_updated": "2022-09-08T21:05:53.773401Z",
    "is_active": true
}

## Delete Task

### Request

`DELETE tasks/api/id/`

### Response

{
    "response": "Object deleted!"
}


