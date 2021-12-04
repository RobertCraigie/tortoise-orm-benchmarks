#!/bin/sh

# setup DB
if [ "$DBTYPE" = "postgres" ]
then
    if [ -z "$GITHUB_ACTIONS" ]
    then
        psql -U postgres -w -c 'drop database tbench';
        psql -U postgres -w -c 'create database tbench';
    else
        # NOTE: assumes this script is being ran from a bench.sh script
        psql -U postgres -w -f ../clean.sql;
    fi
elif [ "$DBTYPE" = "mysql" ]
then
    echo 'DROP DATABASE tbench' | mysql -u root -p$PASSWORD
    echo 'CREATE DATABASE tbench' | mysql -u root -p$PASSWORD
else
    rm -f /dev/shm/db.sqlite3
fi
