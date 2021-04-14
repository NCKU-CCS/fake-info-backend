
# Pull base image
FROM python:3.9

WORKDIR /code/

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --dev

COPY . /code/

WORKDIR /code/sql_app

EXPOSE 8000
