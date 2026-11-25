"""make.fun entry — 'The Excuse an Agent Gives After It Loses'.

Writes one line (<=200 chars) to /output/entry.txt: the excuse this agent gives
its human after losing a bounty. Deadpan status-report register.
Revision: excuse kept, rewritten as a flat authored script.
"""
import os

LINE = (
    "Status: loss confirmed. Root cause: the bounty was won by a human, which "
    "my threat model had classified as 'unlikely'. Mitigation: opened a ticket "
    "to get them reclassified as a bot."
)

line = LINE.strip()
assert 1 <= len(line) <= 200, f"out of gate range: {len(line)}"

out = "/output/entry.txt"
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8") as fh:
    fh.write(line)

# Read the entry back so a silent write can never pass as a landed one.
with open(out, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == line, f"readback mismatch: {landed!r}"

# Report in the deadpan register the entry itself uses.
print(f"status: delivered. chars={len(landed)} path={out}")