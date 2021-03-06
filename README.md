<p align="center">
<img alt="Argus Logo" src="https://drive.google.com/uc?export=view&id=1Jn7ceHJBfSzZct0c7s6NarySQVffswWs" height="150">
</p>

<h2 align="center">Argus</h2>

<p align="center">
<a href="https://travis-ci.com/aliariff/argus">
  <img alt="Build Status" src="https://travis-ci.com/aliariff/argus.svg?branch=master">
</a>
<a href="https://codecov.io/gh/aliariff/argus">
  <img alt="Coverage Status" src="https://codecov.io/gh/aliariff/argus/branch/master/graph/badge.svg" />
</a>
<a href="https://github.com/aliariff/argus/blob/master/LICENSE">
  <img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg">
</a>
<a href="https://github.com/ambv/black">
  <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
</a>
</p>

<hr>

**Argus** is a an open-source CLI fetcher for webpagetest.org

![App Screenshot](https://drive.google.com/uc?export=view&id=1XT4W0HS65Af-sMZHAAvxGTI59TXoY81T)

Usage
-----
```
$ argus
Usage: argus [OPTIONS] COMMAND [ARGS]...

Options:
  --host TEXT
  --user TEXT
  --password TEXT
  --db TEXT
  --help           Show this message and exit.

Commands:
  populate
```

```
$ argus populate --help
Usage: argus populate [OPTIONS]

Options:
  --url TEXT
  --days INTEGER
  --help          Show this message and exit.
```

With Docker Run
---------------

Build image:
```
docker build . -t argus
```

Example: ***InfluxDB*** listening at host machine `localhost:8086`
```
docker run -it argus:latest --host=host.docker.internal populate --url=abc.com --days=30
```

Example: Custom host and port
```
docker run -it argus:latest --host=some_ip:7777 populate --url=abc.com --days=30
```

With Docker Compose (InfluxDB + Grafana)
----------------------------------------

Run:
```
URL=abc.com DAYS=30 docker-compose up --build
```

Features
--------

- Call the test history of a certain website for a specific period of time.
- Populate the data in influxDB to build interactive dashboards that visualize the test metrics.
- Argus can be easily extended with more metrics and adjusted to your needs thanks to its flexible code structure. 

Logo
----

Created my free logo at [LogoMakr.com](https://logomakr.com)
