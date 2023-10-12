# TaskQ

Microservice bundle with FastAPI, Cerely, Flower and RabbitMQ that runs
in Docker.

All modules sit in their own containers and can be developed on the fly (thanks
to "live" mounts in Docker compose).


## Technologies

- Python
- FastAPI
- Cerely
- RabbitMQ
- Flower
- Uvicorn
- Docker

## Standards

- pep8
- flake8
- black
- pymarkdown

## How to run

1. Clone the repository.
2. From the root folder run:

    ```bash
    docker compose up
    ```

3. To create a task and check its status you have three options:
   - `Curl`:

      ```bash
      curl -X 'GET' \
     'http://localhost:8000/create/15' \
     -H 'accept: application/json'

      curl -X 'GET' \
      'http://localhost:8000/ecbbfcb8-c7a3-411b-8e7f-6d5468c1ddba' \
      -H 'accept: application/json'
     ```
   - Using API endpoints or right in `Swagger UI` - http://localhost:8000/docs
   - `Flower` monitoring tool - http://localhost:8001
