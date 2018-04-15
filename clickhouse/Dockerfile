FROM ubuntu:16.04

MAINTAINER Alfimov Dmitry

RUN echo "deb http://repo.yandex.ru/clickhouse/deb/stable/ main/" \
    > /etc/apt/sources.list.d/clickhouse.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv E0C56BD4 

RUN apt-get update
RUN apt-get install -y --allow-unauthenticated \
    clickhouse-server-common \
    clickhouse-client \
    unixodbc odbcinst odbc-postgresql

EXPOSE 9000 8123

CMD ["clickhouse-server", "--config-file=/etc/clickhouse-server/config.xml"]