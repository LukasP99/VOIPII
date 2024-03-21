FROM postgres:15
LABEL maintainer='Lukas Peterek'


COPY *.sql /docker-entrypoint-initdb.d/
COPY *.sh /docker-entrypoint-initdb.d/
