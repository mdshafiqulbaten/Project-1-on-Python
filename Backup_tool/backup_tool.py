import os
import zipfile
from datetime import datetime

def backup(source):
    if not os.path.exists("backups"):
        os.mkdir("backups")

    name = f"backups/backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    with zipfile.ZipFile(name, "w") as zipf:
        for folder, subfolders, files in os.walk(source):
            for file in files:
                path = os.path.join(folder, file)
                zipf.write(path, os.path.relpath(path, source))
    print(f"Backup saved to {name}")

if __name__ == "__main__":
    folder = input("Folder to back up: ")
    backup(folder)
