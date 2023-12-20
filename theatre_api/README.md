# Theatre Service API

Welcome to the Theatre API Service! This API is a Django-based web application designed to manage theatrical performances, theatre sessions, reservations, and related data for a theatre. It provides various endpoints for administrators and authenticated users to interact with the system, offering features such as viewing and filtering performances, managing show sessions, creating reservations, and more.

<img width="1433" alt="Знімок екрана 2023-12-12 о 20 54 23" src="https://github.com/OlehShumov/Theatre-API-Service/assets/145033206/d553f9ca-5e31-4355-b600-81f34662e0bb">


**Demo Credentials:**
- Username: `test_user`
- Password: `123456789`

## Getting Started

### Prerequisites

Before you begin, make sure you have the following tools and technologies installed:

- Python (>=3.6)
- Django
- Django REST framework

## Installing / Getting started
> A quick introduction of the setup you need to get run a project.

### Using Git
1. Clone the repo:
```shell
git clone https://github.com/OlehShumov/Theatre-API-Service.git
```
2. You can open project in IDE and configure .env file using [.env.sample](.env.sample) file as an example.
<details>
<summary>Parameters for .env file:</summary>

- **POSTGRES_DB**: `Name of your DB`
- **POSTGRES_USER**: `Name of your user for DB`
- **POSTGRES_PASSWORD**: `Your password in DB`
- **POSTGRES_HOST** `Host of your DB`
</details>

3. Run docker-compose command to build and run containers:
```shell
docker-compose up --build
```
### Using Docker Hub
1. Login into the Docker:
```shell
docker login
```

2. Pull the project:
```shell
docker pull olegsh26/theatre_api-app:latest

```

3. Run the containers:
```shell
docker-compose up
```


> To access browsable api, use http://localhost:8000/api/theatre/
> 
> Use the following admin user:
> - username: test_user
> - Password: 123456789

## API Endpoints
<details>
  <summary>Plays</summary>

- **List Plays**: `GET /api/theatre/plays/`
- **Create Plays**: `POST /api/theatre/plays/`
- **Retrieve Plays**: `GET /api/theatre/plays/{play_id}/`
- **Update Plays**: `PUT /api/theatre/plays/{play_id}/`
- **Partial Update** `PATCH /api/theatre/plays/{play_id}/`
- **Delete Plays**: `DELETE /api/theatre/plays/{play_id}/`
</details>

<details>
  <summary>Performances</summary>
  
- **List Performances**: `GET /api/theatre/performances/`
- **Create Performances**: `POST /api/theatre/performances/`
- **Retrieve Performances**: `GET /api/theatre/performances/{performance_id}/`
- **Update Performances**: `PUT /api/theatre/performances/{performance_id}/`
- **Partial Update** `PATCH /api/theatre/performances/{performance_id}/`
- **Delete Performances**: `DELETE /api/theatre/performances/{performance_id}/`
</details>

<details>
  <summary>Reservations</summary>
  
- **List Reservations**: `GET /api/theatre/reservations/`
- **Create Reservation**: `POST /api/theatre/reservations/`
- **Retrieve Reservation**: `GET /api/theatre/reservations/{reservation_id}/`
- **Update Reservation**: `PUT /api/theatre/reservations/{reservation_id}/`
- **Partial Update** `PATCH /api/theatre/reservations/{reservation_id}/`
- **Delete Reservation**: `DELETE /api/theatre/reservations/{reservation_id}/`
</details>

<details>
  <summary>Actors</summary>
  
- **List Actors**: `GET /api/theatre/actors/`
- **Create Actor**: `POST /api/theatre/actors/`
- **Retrieve Actor**: `GET /api/theatre/actors/{actor_id}/`
- **Update Actor**: `PUT /api/theatre/actors/{actor_id}/`
- **Partial Update** `PATCH /api/theatre/actors/{actor_id}/`
- **Delete Actor**: `DELETE /api/theatre/actors/{actor_id}/`
</details>

<details>
  <summary>Genres</summary>
  
- **List Genres**: `GET /api/theatre/genres/`
- **Create Genre**: `POST /api/theatre/genres/`
- **Retrieve Genre**: `GET /api/theatre/genres/{genre_id}/`
- **Update Genre**: `PUT /api/theatre/genres/{genre_id}/`
- **Partial Update** `PATCH /api/theatre/genres/{genre_id}/`
- **Delete Genre**: `DELETE /api/theatre/genres/{genre_id}/`
</details>

<details>
  <summary>Theathe halls</summary>
  
- **List Theathe halls**: `GET /api/planetarium/theatres/`
- **Create Theathe hall**: `POST /api/planetarium/theatres/`
- **Retrieve Theathe hall**: `GET /api/planetarium/theatres/{theatre_id}/`
- **Update Theathe hall**: `PUT /api/planetarium/theatres/{theatre_id}/`
- **Partial Update** `PATCH /api/planetarium/theatres/{theatre_id}/`
- **Delete Theathe hall**: `DELETE /api/planetarium/theatres/{theatre_id}/`
</details>

## DB Structure<img width="840" alt="Знімок екрана 2023-12-12 о 22 04 50" src="https://github.com/OlehShumov/Theatre-API-Service/assets/145033206/f2ccd646-8527-407f-a6fb-5b45883b7b47">




## Authentication
- The API uses token-based authentication for user access. Users need to obtain an authentication token by logging in.
- Administrators and authenticated users can access all endpoints, but only administrators can change information about astronomy shows, show sessions, and related entities. Each authenticated user can access and create their own reservations.

## Documentation
- The API is documented using the OpenAPI standard.
- Access the API documentation by running the server and navigating to http://localhost:8000/api/doc/swagger/ or http://localhost:8000/api/doc/redoc/.

## Contributing

Feel free to contribute to these enhancements, and let's make our Planetarium Service API even better!
