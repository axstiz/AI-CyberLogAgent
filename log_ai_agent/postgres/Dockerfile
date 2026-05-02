FROM postgres:18

COPY init-db.sql /docker-entrypoint-initdb.d/init-db.sql

RUN chmod 0555 /docker-entrypoint-initdb.d/init-db.sql