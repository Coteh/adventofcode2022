#!/bin/sh

python -m pytest

if [ "$?" != 0 ]; then
    >&2 echo "pytest tests failed"
    exit 1
fi

max=25

for i in `seq 1 $max`; do
    val=`printf %02d $i`
    if [ -d "$val" ]; then
        echo "Testing Day $val test"
        "./$val/$val.py" "./$val/input_test" | diff "$val/expected_test" -
        if [ "$?" != 0 ]; then
            >&2 echo "Day $val test file failed"
            exit 1
        fi
        for t in `seq 1 5`; do
            if [ -f "$val/expected_test$t" ]; then
                echo "Testing Day $val test $t"
                "./$val/$val.py" "./$val/input_test$t" | diff "$val/expected_test$t" -
                if [ "$?" != 0 ]; then
                    >&2 echo "Day $val test file $t failed"
                    exit 1
                fi
            fi
        done
        echo "Testing Day $val real"
        "./$val/$val.py" "./$val/input" | diff "$val/expected" -
        if [ "$?" != 0 ]; then
            >&2 echo "Day $val failed"
            exit 1
        fi
        echo "Day $val passed!"
    fi
done
