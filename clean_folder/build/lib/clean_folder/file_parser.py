import sys
from pathlib import Path
import constants

def get_extensions(filename: str) -> str:
    return Path(filename).suffix[1:].upper()

def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'other'):
                constants.FOLDERS.append(item)
                scan(item)
            continue
        else:
            ext = get_extensions(item.name)
            full_name = folder / item.name
            if not ext:
                constants.MY_OTHER.append(full_name)
            else:
                try:
                    container = constants.REGISTER_EXTENSION[ext]
                    constants.EXTENSION.add(ext)
                    container.append(full_name)
                except KeyError:
                    constants.UNKNOWN.add(ext)
                    constants.MY_OTHER.append(full_name)

if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    scan(Path(folder_for_scan))