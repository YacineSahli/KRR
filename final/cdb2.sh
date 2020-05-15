#! /bin/bash

python3 dbgen/dbq2.py -i yes -s 4000000 -c 0.2 > dbs/db2yes.lp
python3 dbgen/dbq2.py -i no -s 4000000 -c 0.2 > dbs/db2no.lp
