

from pathlib import Path
from collections import Counter

import numpy as np
from PIL import Image

ROOT = Path("datasets/plantseg/plantseg/annotations")
SPLITS = ["train", "val", "test"]

for split in SPLITS:
    folder = ROOT / split
    value_counts = Counter()
    mask_count = 0
    unusual_masks = 0

    for path in folder.rglob("*.png"):
        with Image.open(path) as image:
            mask = np.asarray(image.convert("L"))

        values, counts = np.unique(mask, return_counts=True)
        value_counts.update({
            int(value): int(count)
            for value, count in zip(values, counts)
        })

        if not set(values.tolist()).issubset({0, 1}):
            unusual_masks += 1

        mask_count += 1

    print(f"\n{split.upper()}")
    print(f"Masks checked: {mask_count:,}")
    print(f"Total pixels with value 0: {value_counts[0]:,}")
    print(f"Total pixels with value 1: {value_counts[1]:,}")
    print(f"Masks containing other values: {unusual_masks}")

print("\nMask value check complete.")
