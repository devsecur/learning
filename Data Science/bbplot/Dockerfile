FROM r-base

COPY . /usr/local/src/myscripts
WORKDIR /usr/local/src/myscripts
RUN apt-get update
RUN apt-get install -y libcurl4-openssl-dev libssl-dev
RUN r test.R
