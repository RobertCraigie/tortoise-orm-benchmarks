#!/bin/sh

cd $(dirname $0)

set -ex

PYPY=`python -V | grep PyPy`

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
