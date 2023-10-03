FROM postgres



ENV PG_MASTER_DB="autoprint"


#usuario root da base de dados
ENV ROOT_USER="narciso"
ENV ROOT_PASSWORD="2001"

#usuario de replicacao
ENV REP_USER="nany"
ENV REP_PASS="2001"


#CONFIGURACOES
RUN echo "wal_level = logical" >> /usr/share/postgresql/postgresql.conf.sample && \
    echo "max_replication_slots = 10" >> /usr/share/postgresql/postgresql.conf.sample && \
    echo "max_wal_senders = 10" >> /usr/share/postgresql/postgresql.conf.sample && \
    echo "listen_addresses = '*'" >> /usr/share/postgresql/postgresql.conf.sample && \
    echo "host    all             all             0.0.0.0/0            md5" >> /etc/postgresql/pg_hba.conf


#EXPOR A PORTA DA BASE DE DADOS
EXPOSE 5432

COPY init-replication.sh /docker-entrypoint-initdb.d/

#sudo docker volume create autoprintvolume
#sudo docker build -t postgresautoprint .
#sudo docker run --name postgresautoprint --restart always -e POSTGRES_PASSWORD=mysecretpassword -v autoprintvolume:/var/lib/postgresql/data -d postgresautoprint

