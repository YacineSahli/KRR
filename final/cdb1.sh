#! /bin/bash

python3 dbgen/dbq1.py -i yes -s 1000 -c 0.2 > dbs/db1yes.lp
python3 dbgen/dbq1.py -i no -s 1000 -c 0.2 > dbs/db1no.lp
