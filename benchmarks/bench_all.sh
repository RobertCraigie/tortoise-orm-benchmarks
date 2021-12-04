#!/bin/sh

set -ex

cd $(dirname $0)

echo > results

# DBTYPE=sqlite ./bench.sh $1
python -V | grep PyPy || DBTYPE=postgres ./bench.sh $1

# TODO
# DBTYPE=mysql ./bench.sh $1

cat results
