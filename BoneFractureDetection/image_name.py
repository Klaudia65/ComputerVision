import os
import glob

folder = "demo"

images = sorted(glob.glob(os.path.join(folder, "demo*.jpg")))

for idx, img_path in enumerate(images, start=1):
    temp_name = f"temp_demo_{idx}.jpg"
    temp_path = os.path.join(folder, temp_name)
    os.rename(img_path, temp_path)

temp_images = sorted(glob.glob(os.path.join(folder, "temp_demo_*.jpg")))
for idx, img_path in enumerate(temp_images, start=1):
    new_name = f"demo{idx}.jpg"
    new_path = os.path.join(folder, new_name)
    os.rename(img_path, new_path)
    print(f"Renamed {img_path} -> {new_path}")

print("Renaming completed.")