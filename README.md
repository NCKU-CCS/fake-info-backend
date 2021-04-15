# Chrome extension backend
The repo is a docker base backend included API-server and database for fake info chrome extension.
## Outline
*  [Getting Started](Getting Started)
## Getting Started
### Prerequistes
* docker 20.10.0

### Usage
#### sample.env
You have to set sample.env file to make this repo work. After setting the sample.env, change file name of sample.env to .env .
'''
POSTGRES_USER=yourname
POSTGRES_PASSWORD=yourpassword
POSTGRES_SERVER=yourserver
POSTGRES_PORT=yourport
POSTGRES_DB=yourdb
'''
#### build docker container
'''
docker-compose up -d --build
'''
