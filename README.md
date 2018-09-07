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

**Argus** is a ...

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

Via Docker
~~~~~~~~~~

```
docker build . -t argus

docker run -it argus:latest --host=host.docker.internal populate --url=abc.com --days=30
```


Features
--------
