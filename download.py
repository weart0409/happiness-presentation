import kagglehub
import shutil
from pathlib import Path

# Download latest version
cache_path = kagglehub.dataset_download("unsdsn/world-happiness")
print("Path to dataset files in cache:", cache_path)

# Optional: Copy files to local 'data' folder for easy access
target_dir = Path(__file__).parent / "data"
target_dir.mkdir(exist_ok=True)

for file in Path(cache_path).glob("*.csv"):
    dest = target_dir / file.name
    shutil.copy2(file, dest)
    print(f"Copied {file.name} -> {dest}")
