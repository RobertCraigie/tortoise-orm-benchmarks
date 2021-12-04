#!/bin/sh

# setup DB
if [ "$DBTYPE" = "postgres" ]
then
    if [ -z "$GITHUB_ACTIONS" ]
    then
        psql -U postgres -w -c 'drop database tbench';
        psql -U postgres -w -c 'create database tbench';
    else
        psql -U postgres -w -c 'SELECT "TRUNCATE " || input_table_name || " CASCADE;" AS truncate_query FROM(SELECT table_schema || "." || table_name AS input_table_name FROM information_schema.tables WHERE table_schema NOT IN ("pg_catalog", "information_schema") AND table_schema NOT LIKE "pg_toast%") AS information;';
    fi
elif [ "$DBTYPE" = "mysql" ]
then
    echo 'DROP DATABASE tbench' | mysql -u root -p$PASSWORD
    echo 'CREATE DATABASE tbench' | mysql -u root -p$PASSWORD
else
    rm -f /dev/shm/db.sqlite3
fi
