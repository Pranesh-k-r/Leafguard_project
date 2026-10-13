
from pathlib import Path

dataset_path = Path("datasets/plantdoc/PlantDoc-Dataset")

print("\nPlantDoc dataset structure")
print("=" * 60)

for item in sorted(dataset_path.iterdir()):

    if item.is_dir():

        images = [
            file
            for file in item.rglob("*")
            if file.is_file()
            and file.suffix.lower() in {
                ".jpg",
                ".jpeg",
                ".png",
                ".bmp",
                ".webp",
            }
        ]

        print(f"{item.name}: {len(images):,} images")

print("\nDone.")