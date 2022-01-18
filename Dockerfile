FROM ubuntu:18.04
USER root

# Needed to support utf-8 symbols in stdout
RUN apt-get clean && apt-get update && apt-get install -y locales
RUN locale-gen en_US.UTF-8
RUN update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

RUN apt-get install -y python3

RUN mkdir /httpserver
COPY httpserver.py /httpserver/httpserver.py
COPY *.json /httpserver/

# Needed to support utf-8 symbols in stdout
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
WORKDIR /httpserver

CMD ["/bin/bash", "-c", "python3 httpserver.py"]

