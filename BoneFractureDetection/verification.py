import os
import hashlib

target_path = "external_source.jpg"

dataset_dirs = [
    "Break-bone-3/train/images",
    "Break-bone-3/valid/images",
    "Break-bone-3/test/images"
]

def file_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

target_hash = file_hash(target_path)
found = False

for folder in dataset_dirs:
    for fname in os.listdir(folder):
        fpath = os.path.join(folder, fname)
        if os.path.isfile(fpath):
            if file_hash(fpath) == target_hash:
                print(f"Images found: {fpath}")
                found = True

if not found:
    print("Images not found")