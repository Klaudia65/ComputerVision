from PIL import Image
import glob
import os

input_folder = "."
output_folder = "./converted"

os.makedirs(output_folder, exist_ok=True)

for img_path in glob.glob(os.path.join(input_folder, "external_source*.jpg")):
    img = Image.open(img_path).convert("RGB")
    img = img.resize((640, 640))
    out_path = os.path.join(output_folder, os.path.basename(img_path))
    img.save(out_path)
    print(f"Saved: {out_path}")

print("All images converted and resized.")