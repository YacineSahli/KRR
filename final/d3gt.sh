#! /bin/bash

clingo dbs/db3yes.lp gen\&test/q3gt.lp --stats
clingo dbs/db3no.lp gen\&test/q3gt.lp --stats
