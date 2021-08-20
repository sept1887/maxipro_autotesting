# MaxiPRO

You have to install Docker for running tests.

It works with `selenoid`.

Selenoid is installed on dev-1 server  (http://192.168.14.19:4444/wd/hub/)

Config file: `tests/conftest.py`.

Selenoid UI: [http://192.168.14.19:8081/#/](http://192.168.14.19:8081/#/)

Run tests:

```sh
docker-compose up -d

# запуск тестов в 4 потока на https://maxipro.ru/ 
docker-compose run pythonservice pytest -v -n=4 /tests/

# запуск тестов в 4 потока на https://maxipro-develop.dclouds.ru/
docker-compose run pythonservice pytest -v -n=4 --env=develop --url=https://maxipro-develop.dclouds.ru/ /tests/

docker-compose down
```