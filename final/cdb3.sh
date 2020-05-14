#! /bin/bash

python3 dbgen/dbq3.py -i yes -s 4000000 -c 0.2 > dbs/db3yes.lp
python3 dbgen/dbq3.py -i no -s 4000000 -c 0.2 > dbs/db3no.lp
