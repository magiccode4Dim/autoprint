#!/bin/bash
set -e

# inicia o servidor
pg_ctl restart -D /var/lib/postgresql/data


psql -U postgres -c "CREATE USER ${ROOT_USER} WITH PASSWORD '${ROOT_PASSWORD}';"

# Superuser
psql -U postgres -c "ALTER USER ${ROOT_USER} WITH SUPERUSER;"


# Crie a base de dados, se ela não existir
psql -U postgres -c "CREATE DATABASE ${PG_MASTER_DB};"


#cria o usuario de replicacao
psql -U postgres -d ${PG_MASTER_DB} -c "CREATE ROLE ${REP_USER} WITH REPLICATION LOGIN PASSWORD '${REP_PASS}';"

#atribui privilegios do usuario de replicacao sobre a base de dados
psql -U postgres -d ${PG_MASTER_DB} -c "GRANT ALL PRIVILEGES ON DATABASE ${PG_MASTER_DB} TO ${REP_USER};"

psql -U postgres -d ${PG_MASTER_DB} -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ${REP_USER};"


