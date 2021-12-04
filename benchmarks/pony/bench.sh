#!/bin/sh

cd $(dirname $0)
set -ex

# setup DB
../db.sh

# Test A → Insert
python -m test_a

# Test B → Transactioned Intsert
python -m test_b

# Test C → Bulk Insert
# Not supported

# Test D → Filter on level
python -m test_d

# Test E → Filter limit 20
python -m test_e

# Test F → Get
python -m test_f

# Test G → dict
python -m test_g

# Test H → tuple
python -m test_h

# Test I → Update full
python -m test_i

# Test J → Update Partial
python -m test_j

# Test K → Delete
python -m test_k
