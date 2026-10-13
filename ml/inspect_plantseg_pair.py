
from pathlib import Path
import numpy as np
from PIL import Image

ROOT = Path("datasets/plantseg/plantseg")

image_path = ROOT / "images" / "train" / "apple_black_rot_1.jpg"
mask_path = ROOT / "annotations" / "train" / "apple_black_rot_1.png"

print("PlantSeg mask verification")
print("=" * 50)

if not image_path.exists():
    raise FileNotFoundError(f"Image not found: {image_path}")

if not mask_path.exists():
    raise FileNotFoundError(f"Mask not found: {mask_path}")

with Image.open(image_path) as image:
    print(f"Image size: {image.size}")
    print(f"Image mode: {image.mode}")

with Image.open(mask_path) as mask:
    mask_array = np.asarray(mask)
    print(f"Mask size: {mask.size}")
    print(f"Mask mode: {mask.mode}")

values, counts = np.unique(mask_array, return_counts=True)

print("\nPixel counts:")
for value, count in zip(values, counts):
    percentage = count / mask_array.size * 100
    print(f"  Value {value}: {count:,} pixels ({percentage:.2f}%)")

print("\nDone.")
