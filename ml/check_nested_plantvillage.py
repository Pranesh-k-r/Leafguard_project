
from pathlib import Path

path = Path("datasets/plantvillage/PlantVillage/PlantVillage")

print("\nNested PlantVillage contents")
print("=" * 60)

for item in sorted(path.iterdir()):
    if item.is_dir():
        images = [
            f for f in item.rglob("*")
            if f.is_file()
            and f.suffix.lower() in {
                ".jpg",
                ".jpeg",
                ".png",
                ".bmp",
                ".webp",
            }
        ]

        print(f"{item.name}: {len(images):,} images")

    elif item.is_file():
        print(f"FILE: {item.name}")

print("\nDone.")