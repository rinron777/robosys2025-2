#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 rinron777
# SPDX-License-Identifier: BSD-3-Clause

import sys

if len(sys.argv) < 2:
    print("usage: calc [plus|minus|times|div]", file=sys.stderr)
    sys.exit(1)

op = sys.argv[1]

ans = None
for line in sys.stdin:
    try:
        value = int(line)
    except:
        value = float(line)

    if ans is None:
        ans = value
    else:
        if op == "plus":
            ans += value
        elif op == "minus":
            ans -= value
        elif op == "times":
            ans *= value
        elif op == "div":
            ans /= value
        else:
            print("unknown operation", file=sys.stderr)
            sys.exit(1)

print(ans)

