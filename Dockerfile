FROM python:3.6

RUN pip install pipenv

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN mkdir /app
WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

COPY . /app
RUN pipenv install --deploy --system

ENTRYPOINT ["argus"]
