#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 rinron777
#SPDX-License-Identifier: GPL-3-Clause

ng () {
       echo "Error at line ${1}"
       res=1
}

res=0

# plus
out=$(seq 5 | ./calc plus)
[ "${out}" = 15 ] || ng "$LINENO"

# minus
out=$(seq 5 | ./calc minus)
[ "${out}" = -13 ] || ng "$LINENO"

# times
out=$(seq 5 | ./calc times)
[ "${out}" = 120 ] || ng "$LINENO"

# div
out=$(seq 5 | ./calc div)
[ "${out}" = 0.008333333333333333 ] || ng "$LINENO"

[ "${res}" = 0 ] && echo OK
exit $res

