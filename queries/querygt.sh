#! /bin/bash

python3 "gtq"$1".py" $2
clingo $2 "q"$1"gt.lp"
rm "q"$1"gt.lp"
