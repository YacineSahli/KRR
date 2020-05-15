#! /bin/bash

clingo dbs/db2yes.lp gen\&test/q2gt.lp --stats
clingo dbs/db2no.lp gen\&test/q2gt.lp --stats
