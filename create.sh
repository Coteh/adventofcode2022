#!/bin/sh

DAY="$1"

if [ "$DAY" == "" ]; then
    >&2 echo "Please provide the day"
    exit 1
fi

mkdir "$DAY"
if [ "$?" != "0" ]; then
    exit 1
fi

cat << EOF > "$DAY/$DAY.py"
#!/usr/bin/env python

import sys

def process_input(file_name):
    with open(file_name) as f:
        data = f.read()
        return data

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write("Please provide input filename")
        sys.exit(1)
    data = process_input(sys.argv[1])
    print(data)
EOF

chmod +x "$DAY/$DAY.py"
git add "$DAY/$DAY.py"
git update-index --chmod=+x "$DAY/$DAY.py"
