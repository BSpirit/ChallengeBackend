# ChallengeBackend

## Requirements

Docker and docker-compose can be used to run the application in your local environnement.

1. Install Docker
https://docs.docker.com/get-docker/

2. Install Docker compose
https://docs.docker.com/compose/install/

3. Set environnement variables: .env file must be created at the root of the repo.

.env file content:
```
export SECRET_KEY=<a-secret-key>
export SPOTIFY_CLIENT_ID=<spotify-api-client-id>
export SPOTIFY_CLIENT_SECRET=<spotify-api-client-secret>

export POSTGRES_DB=postgres
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=postgres
```

## Run application

1. Build the application
```
docker-compose build
```

2. Run the application
```
docker-compose up
```

3. Run migrations (if necessary, i.e. when the container is running for the first time)
```
docker container exec <container-ID> python manage.py migrate
```

*NB*: The app listens on port 8000. docker-compose should only be used in a dev environnement.


# Subject

Your goal is to create an app using the [spotify web api](https://developer.spotify.com/documentation/web-api/). You can make for example a [Flask](https://flask.palletsprojects.com/en/1.1.x/) or [Django rest framework](https://www.django-rest-framework.org/) project, it has to be able to authenticate to Spotify to fetch the new releases. Your job is to add two new features:
- A way to fetch data from spotify’s new releases API (/v1/browse/new-releases) and persist in a Postgresql DB (mandatory)
- A route : `/api/artists/` returning a JSON containing informations about artists that have released new tracks recently, from your local copy of today’s spotify’s new releases.

## Project Structure
The spotify auth is provided by us: (follows spotify web api.): it is located in `spotify_auth.py`.
The flow ends with a call to `/auth/callback/` which will give you the necessary access tokens.
To use it, we will provide you with the necessary: CLIENT_ID and CLIENT_SECRET.
Feel free to move it and re-organise as you please, we expect a well organised and clean code.
  
  
## Tech Specifications
- Be smart in your token usage (no unnecessary refreshes)
- Don’t request spotify artists at each request we send you
- The way you store the artists in Postgresql DB is going to be important use an ORM.
- As stated above, to test your server we will `GET /api/artists/` and we expect a nicely organised payload of artists. Make sure to use proper serialization and handle http errors.

All stability, performance, efficiency adds-up are highly recommended.
