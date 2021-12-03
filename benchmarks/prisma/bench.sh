#!/bin/sh

cd $(dirname $0)

PYPY=`python -V | grep PyPy`
TEST=$TEST
if [[ -z $TEST ]]; then
    TEST="1";
fi

# setup DB
../db.sh

rm schema.prisma
rm models.prisma

cp $TEST.prisma models.prisma

if [ "$DBTYPE" = "postgres" ]
then
    echo "PostgreSQL tests are not supported yet";
    exit 1;
elif [ "$DBTYPE" = "mysql" ]
then
    echo "MySQL tests are not supported yet";
    exit 1;
else
    cat sqlite.prisma models.prisma > schema.prisma
fi

python -m prisma db push


if [ -z "$PYPY" ]
then
    # run uvloop benchmarks
    PYTHONUNBUFFERED=x UVLOOP=1 python -m bench
else
    # run regular loop benchmarks
    PYTHONUNBUFFERED=x python -m bench
fi
