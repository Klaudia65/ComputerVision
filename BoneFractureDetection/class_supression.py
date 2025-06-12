import os

classes_to_remove = [7, 8, 9, 10]  # null, oblique, spiral, Intra-articular

splits = ["train", "valid", "test"]
base_dir = "Break-bone-3"

for split in splits:
    labels_dir = os.path.join(base_dir, split, "labels")
    images_dir = os.path.join(base_dir, split, "images")
    for fname in os.listdir(labels_dir):
        if fname.endswith(".txt"):
            label_path = os.path.join(labels_dir, fname)
            with open(label_path, "r") as f:
                lines = f.readlines()
            to_delete = any(line.strip() and int(line.split()[0]) in classes_to_remove for line in lines)
            if to_delete:
                os.remove(label_path)
                base_name = os.path.splitext(fname)[0]
                for ext in [".jpg", ".jpeg", ".png"]:
                    img_path = os.path.join(images_dir, base_name + ext)
                    if os.path.exists(img_path):
                        os.remove(img_path)
print("Image and label removal completed.")