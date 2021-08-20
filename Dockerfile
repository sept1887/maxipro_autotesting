FROM python:3.7

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3-pip -y
RUN pip3 install pipenv pytest pytest-rerunfailures pytest-xdist requests selenium
RUN mkdir /pytest_cache

