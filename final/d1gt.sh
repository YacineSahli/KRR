#! /bin/bash

clingo dbs/db1yes.lp gen\&test/q1gt.lp --stats
clingo dbs/db1no.lp gen\&test/q1gt.lp --stats
