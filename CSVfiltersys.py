#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Rintarou Matunaga
# SPDX-License-Identifier: BSD-3-Clause

def filter_rows(rows: list[list[str]]) -> list[list[str]]:
    
    if not rows:
        return []

    result = []

    header = rows[0]
    result.append(header)

    for r in rows[1:]:
        if len(r) < 2:
            continue
        try:
            age = int(r[1])
            if age >= 20:
                result.append(r)
        except ValueError:
            
            continue

    return result


def sort_rows(rows: list[list[str]]) -> list[list[str]]:
    
    return sorted(rows, key=lambda x: x[2] if len(x) > 2 else "")

if __name__ == "__main__":
    import sys
    import csv

    reader = csv.reader(sys.stdin)
    rows = list(reader)

    filtered = filter_rows(rows)

    for r in filtered:
        print(",".join(r))


