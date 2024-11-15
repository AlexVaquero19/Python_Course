import activity_modules
from pathlib import Path
from my_module import greet

print(greet('Alejandro'))

file_path = Path("activity_file.txt")
buckup_dir = Path("backup")

activity_modules.list_files_in_directory(Path('.'))
activity_modules.backup_file(file_path, buckup_dir)