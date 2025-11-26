#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Rintarou Matunaga
# SPDX-License-Identifier: BSD-3-Clause

import sys
import csv

def main():
    reader = csv.reader(sys.stdin)
    writer = csv.writer(sys.stdout)

    for row in reader:
        writer.writerow(row)

if __name__ == "__main__":
    main()

