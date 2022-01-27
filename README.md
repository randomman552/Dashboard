# Dashboard
A simple dashboard application designed to be easily configurable.\
Designed to be hosted through docker.

## Docker
I recommend deploying this application with the use of docker compose for ease.\
An example of deployment (with [traefik](https://traefik.io/traefik/) reverse proxy) can be seen below:
```yml
version: '3.9'
services:
  dashboard:
    image: randomman552/dashboard:latest
    container_name: dashboard
    volumes:
      - /storage/dashboard:/data
    labels:
      - "traefik.enable=true"
      - "traefik.http.services.dashboard.loadbalancer.server.port=80"
      - "traefik.http.routers.dashboard.rule=Host(`dashboard.local`)"
      - "traefik.http.routers.dashboard.entrypoints=web,websecure"
      - "traefik.http.routers.dashboard.tls=true"
```

This allows for the mounting of custom styles and config files in the host file system at `/storage/dashboard`

## Environment variables
- `DASHBOARD_PORT` - The port used by gunicorn to present the application.
  - Defaults to 80
- `DASHBOARD_DATA_PATH` - The path where data is located. Allows for customisation of the dashboard.
  - Defaults to `/data`

## Customisation
Customisation of the dashboard program are done through its data path.\
Any files placed within this directory will override the default ones.\
For example, a config.json file here will override the default one contained within the static folder.

This allows for the insertion of custom styles.css, config.json, and any icons or the site favicon itself.

### Config file
TODO: Detail how the config file should be layed out