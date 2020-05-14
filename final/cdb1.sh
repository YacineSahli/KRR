#! /bin/bash

python3 dbgen/dbq1.py -i yes -s 100 -c 0.5 > dbs/db1yes.lp
python3 dbgen/dbq1.py -i no -s 100 -c 0.5 > dbs/db1no.lp