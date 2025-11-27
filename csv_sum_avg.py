#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Rintarou Matunaga
# SPDX-License-Identifier: BSD-3-Clause

import sys
import csv

reader = csv.DictReader(sys.stdin)

sums = {}
counts = {}

for row in reader:
    for key, value in row.items():
        if value.strip() == "":
            continue
        try:
            num = float(value)
            sums[key] = sums.get(key, 0.0) + num
            counts[key] = counts.get(key, 0) + 1
        except ValueError:
            continue  

sorted_keys = sorted(sums.keys())

sum_str = " ".join(f"{k}={sums[k]:.2f}" for k in sorted_keys)
avg_str = " ".join(f"{k}={sums[k]/counts[k]:.2f}" for k in sorted_keys)

print(f"sum: {sum_str}")
print(f"avg: {avg_str}")

