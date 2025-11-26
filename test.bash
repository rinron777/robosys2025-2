#!/bin/bash
set -e  
set -x  

echo "[TEST] CSVsys.py test running..."
cat test/input.csv | python3 CSVsys.py > test/output1.csv

if [ ! -s test/output1.csv ]; then
    echo "ERROR: CSVsys.py output is empty!"
    exit 1
fi

echo "[TEST] CSVfiltersys.py test running..."
cat test/filter_input.csv | python3 CSVfiltersys.py > test/output2.csv

diff -q test/output2.csv test/expected_filter_output.csv

echo "[PASS] All CSV tests passed!"
exit 0

