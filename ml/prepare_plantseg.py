

from pathlib import Path
from PIL import Image
import numpy as np

ROOT = Path("datasets/plantseg/plantseg")
SPLITS = ["train", "val", "test"]
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def find_pairs(split):
    image_dir = ROOT / "images" / split
    mask_dir = ROOT / "annotations" / split
    pairs = []

    for image_path in image_dir.rglob("*"):
        if not image_path.is_file():
            continue
        if image_path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        mask_path = mask_dir / f"{image_path.stem}.png"

        if mask_path.exists():
            pairs.append((image_path, mask_path))

    return pairs


def main():
    print("LEAFGUARD AI - PlantSeg Pair Check")
    print("=" * 45)

    for split in SPLITS:
        pairs = find_pairs(split)
        missing = 0

        image_dir = ROOT / "images" / split
        mask_dir = ROOT / "annotations" / split

        for image_path in image_dir.rglob("*"):
            if image_path.is_file() and image_path.suffix.lower() in IMAGE_EXTENSIONS:
                if not (mask_dir / f"{image_path.stem}.png").exists():
                    missing += 1

        print(f"\n{split.upper()}")
        print(f"Matched image-mask pairs: {len(pairs):,}")
        print(f"Images without matching masks: {missing:,}")

        if pairs:
            image_path, mask_path = pairs[0]
            with Image.open(image_path) as image, Image.open(mask_path) as mask:
                print(f"Sample image size: {image.size}")
                print(f"Sample mask size:  {mask.size}")
                print(f"Sizes match: {image.size == mask.size}")

                mask_array = np.asarray(mask.convert("L"))
                print(f"Mask pixel values: {np.unique(mask_array).tolist()}")

    print("\nPair check complete.")


if __name__ == "__main__":
    main()
