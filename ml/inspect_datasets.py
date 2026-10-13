
from pathlib import Path
from collections import Counter


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_ROOT = PROJECT_ROOT / "datasets"


IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp",
}


def get_images(folder):

    return [
        file
        for file in folder.rglob("*")
        if file.is_file()
        and file.suffix.lower() in IMAGE_EXTENSIONS
    ]


def inspect_dataset(dataset_name):

    dataset_path = DATASET_ROOT / dataset_name

    print("\n" + "=" * 70)
    print(f"DATASET: {dataset_name.upper()}")
    print("=" * 70)

    if not dataset_path.exists():

        print("❌ Dataset folder does not exist")

        return

    images = get_images(dataset_path)

    print(f"Total images: {len(images):,}")

    extensions = Counter(
        image.suffix.lower()
        for image in images
    )

    print("\nImage formats:")

    for extension, count in extensions.items():

        print(
            f"  {extension}: {count:,}"
        )

    print("\nTop-level folders:")

    for folder in sorted(dataset_path.iterdir()):

        if folder.is_dir():

            folder_images = get_images(folder)

            print(
                f"  {folder.name}: "
                f"{len(folder_images):,} images"
            )


DATASETS = [

    "plantvillage",
    "plantdoc",
    "plantseg",
    "paddy_doctor",
    "field_acquired",

]


print()

print("=" * 70)

print(
    "             LEAFGUARD AI DATASET INSPECTOR"
)

print("=" * 70)


for dataset in DATASETS:

    inspect_dataset(dataset)


print("\nInspection complete.")