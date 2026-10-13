
from pathlib import Path


ROOT = Path("datasets/plantseg/plantseg")

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp",
}


def count_images(folder):
    return sum(
        1
        for file in folder.rglob("*")
        if file.is_file()
        and file.suffix.lower() in IMAGE_EXTENSIONS
    )


print("\nPlantSeg dataset")
print("=" * 60)

images_path = ROOT / "images"
annotations_path = ROOT / "annotations"

print(f"Images folder exists: {images_path.exists()}")
print(f"Annotations folder exists: {annotations_path.exists()}")

if images_path.exists():
    print(f"Image files: {count_images(images_path):,}")

if annotations_path.exists():
    print(f"Annotation image files: {count_images(annotations_path):,}")

print("\nImages subfolders:")

if images_path.exists():
    for folder in sorted(images_path.iterdir()):
        if folder.is_dir():
            print(
                f"  {folder.name}: "
                f"{count_images(folder):,} images"
            )

print("\nAnnotation subfolders:")

if annotations_path.exists():
    for folder in sorted(annotations_path.iterdir()):
        if folder.is_dir():
            print(
                f"  {folder.name}: "
                f"{count_images(folder):,} files"
            )

print("\nJSON annotation files:")

for file in sorted(ROOT.glob("*.json")):
    print(f"  {file.name}: {file.stat().st_size:,} bytes")

print("\nDone.")