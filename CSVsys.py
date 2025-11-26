#!/usr/bin/python3
# SPDX-FileCopyrightText: Rintarou Matunaga
# SPDX-License-Identifier: BSD-3-Clause

import sys
import csv
from CSVfiltersys import filter_rows, sort_rows

def main():
    reader = csv.reader(sys.stdin)
    rows = list(reader)

    header = rows[0]
    body = rows[1:]

    filtered = filter_rows(body)
    sorted_rows = sort_rows(filtered)

    writer = csv.writer(sys.stdout)
    writer.writerow(header)
    writer.writerows(sorted_rows)

if __name__ == "__main__":
    main()

