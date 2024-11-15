import os
import certifi
import shutil

def list_files_in_directory(path):
    for file in os.listdir(path):
        print(file)

def backup_file(file_path, buckup_dir):
    shutil.move(file_path, buckup_dir)

print(certifi.where())