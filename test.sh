#!/bin/sh

python -m pytest

if [ "$?" != 0 ]; then
    >&2 echo "pytest tests failed"
    exit 1
fi

max=25

DATA_DIR="./data/2022"

for i in `seq 1 $max`; do
    val=`printf %02d $i`
    if [ -d "$val" ]; then
        echo "Testing Day $val test"
        "./$val/$val.py" "${DATA_DIR}/$val/sample" | diff "${DATA_DIR}/$val/expected_sample" -
        if [ "$?" != 0 ]; then
            >&2 echo "Day $val test file failed"
            exit 1
        fi
        for t in `seq 2 6`; do
            if [ -f "${DATA_DIR}/$val/expected_sample$t" ]; then
                echo "Testing Day $val test $t"
                "./$val/$val.py" "${DATA_DIR}/$val/sample$t" | diff "${DATA_DIR}/$val/expected_sample$t" -
                if [ "$?" != 0 ]; then
                    >&2 echo "Day $val test file $t failed"
                    exit 1
                fi
            fi
        done
        echo "Testing Day $val real"
        "./$val/$val.py" "${DATA_DIR}/$val/input" | diff "${DATA_DIR}/$val/expected" -
        if [ "$?" != 0 ]; then
            >&2 echo "Day $val failed"
            exit 1
        fi
        echo "Day $val passed!"
    fi
done
