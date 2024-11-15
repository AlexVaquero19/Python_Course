import os
import sys
import shutil
from pathlib import Path

for file in os.listdir(os.getcwd()):
    print(f"File {file}")

with open("activity_file.txt", "w") as f:
    f.write(f"Version: {sys.version}")

example_file = Path("activity_file.txt")

print(f"Moving file {example_file.name} to example_dir/")
shutil.move(example_file, Path(f"example_dir/{example_file.name}"))