FROM ubuntu:14.04

MAINTAINER carlad "https://github.com/Bezumova»

# Install packages for building ruby
RUN apt-get update
RUN apt-get install -y --force-yes git python3
RUN apt-get clean

RUN git clone https://github.com/Bezumova/trpo /root/trpo