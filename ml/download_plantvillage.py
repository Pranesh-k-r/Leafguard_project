
import kagglehub

path = kagglehub.dataset_download(
    "emmarex/plantdisease",
    output_dir=r"C:\Users\PRANESH K R\LeafGuard_AI\datasets\plantvillage"
)

print("PlantVillage dataset downloaded to:")
print(path)