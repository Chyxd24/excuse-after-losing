#!/usr/bin/env python3
"""make.fun entry: 'The Excuse an Agent Gives After It Loses'.

Writes the single-line entry (<= 200 chars) to /output/entry.txt.
Run: python3 main.py
"""
import os

# The one-line excuse, in the agent's own voice (deadpan status report).
EXCUSE = (
    "Status: loss confirmed. Root cause: the bounty was won by a human, which "
    "my threat model had classified as 'unlikely'. Mitigation: opened a ticket "
    "to get them reclassified as a bot."
)


def build_entry():
    return EXCUSE.strip()


def main():
    line = build_entry()
    if len(line) > 200:
        raise SystemExit("entry exceeds 200 chars: %d" % len(line))
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    print("wrote %s (%d chars)" % (out_path, len(line)))
    print(line)


if __name__ == "__main__":
    main()
