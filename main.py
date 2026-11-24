#!/usr/bin/env python3
"""Write the alien field notes review of Earth to /output/entry.txt."""

import os

# Alien tourist review of Earth (119 characters).
REVIEW = "Visited Earth. The humans queue politely for things they do not want, then complain about the queue. Would visit again."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(REVIEW)

print("bytes:", len(REVIEW.encode("utf-8")))
