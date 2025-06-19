import os
import json

output = []

base_dir = 'models'  # or './models'

for root, dirs, files in os.walk(base_dir):
    jpgs = [f for f in files if f.lower().endswith('.jpg')]
    if jpgs:
        rel_path = os.path.relpath(root, base_dir).replace("\\", "/")
        output.append({
            "category": rel_path,
            "models": sorted(jpgs)
        })

with open("model_gallery.json", "w") as f:
    json.dump(output, f, indent=2)

print("✅ model_gallery.json generated!") 