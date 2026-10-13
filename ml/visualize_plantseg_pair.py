

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

ROOT = Path("datasets/plantseg/plantseg")

image_path = ROOT / "images" / "train" / "apple_black_rot_1.jpg"
mask_path = ROOT / "annotations" / "train" / "apple_black_rot_1.png"

image = np.asarray(Image.open(image_path).convert("RGB"))
mask = np.asarray(Image.open(mask_path).convert("L"))

# PlantSeg's sample mask uses 0 and 1.
binary_mask = mask > 0

# Overlay the mask in red to make annotated pixels visible.
overlay = image.copy()
overlay[binary_mask] = (
    0.6 * overlay[binary_mask] + 0.4 * np.array([255, 0, 0])
).astype(np.uint8)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(image)
axes[0].set_title("Original leaf image")

axes[1].imshow(binary_mask, cmap="gray", vmin=0, vmax=1)
axes[1].set_title("Annotation mask")

axes[2].imshow(overlay)
axes[2].set_title("Mask overlay")

for axis in axes:
    axis.axis("off")

plt.tight_layout()
plt.show()
