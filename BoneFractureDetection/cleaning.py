import os

labels_dir = r"Break-bone-3/train/labels"  # adapte le chemin pour valid/test si besoin
label_count = {}

# Nombre de classes (doit correspondre à la longueur de names dans data.yaml)
num_classes = 11

# Initialiser le compteur pour chaque label
for i in range(num_classes):
    label_count[i] = 0

for fname in os.listdir(labels_dir):
    if fname.endswith(".txt"):
        with open(os.path.join(labels_dir, fname)) as f:
            for line in f:
                if line.strip():
                    idx = int(line.split()[0])
                    label_count[idx] += 1

for idx, count in label_count.items():
    print(f"Label {idx}: {count} objects labeled")