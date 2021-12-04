#!/bin/sh

cd $(dirname $0)

PYPY=`python -V | grep PyPy`

set -ex

# setup DB
../db.sh

if [ -z "$PYPY" ]
then
    # run uvloop benchmarks
    PYTHONUNBUFFERED=x UVLOOP=1 python -m bench
else
    # run regular loop benchmarks
    PYTHONUNBUFFERED=x python -m bench
fi
