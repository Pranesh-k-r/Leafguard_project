
import kagglehub

path = kagglehub.dataset_download(
    "abdulhasibuddin/plant-doc-dataset",
    output_dir=r"C:\Users\PRANESH K R\LeafGuard_AI\datasets\plantdoc"
)

print("PlantDoc dataset downloaded to:")
print(path)