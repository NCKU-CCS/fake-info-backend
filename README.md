# Chrome extension backend
The repo is a docker base backend included API-server and database for fake info chrome extension.
* [front end](https://github.com/NCKU-CCS/fake-info-extension)
## Getting Started
### Prerequisites
* docker 20.10.0
* python 3.9.1
    * pipenv 2020.11.15
### Running Production

* Create environment file
```
cp sample.env .env
```
* build docker container
```
docker-compose up -d --build
```
