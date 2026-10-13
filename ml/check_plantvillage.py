
from pathlib import Path

dataset_path = Path("datasets/plantvillage/PlantVillage")

print("\nPlantVillage disease classes")
print("=" * 60)

for folder in sorted(dataset_path.iterdir()):
    if folder.is_dir():
        images = [
            file
            for file in folder.rglob("*")
            if file.is_file()
            and file.suffix.lower() in {
                ".jpg",
                ".jpeg",
                ".png",
                ".bmp",
                ".webp",
            }
        ]

        print(f"{folder.name}: {len(images):,} images")

print("\nDone.")