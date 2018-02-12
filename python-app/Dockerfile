FROM ubuntu:17.10

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-dev libmysqlclient-dev
RUN apt-get install -y libmysqlclient-dev
RUN apt-get install -y python3-pymysql

COPY requirements.txt /usr/src/app
RUN pip3 install -r requirements.txt

# copy all files into the container
COPY . /usr/src/app

EXPOSE 5000 3306

RUN python3 run.py
