from pathlib import Path
from normalize import normalize
import shutil
import sys
import file_parser as parser
import constants

def handle_media(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_other(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_arhive(filename: Path, target_folder: Path) -> None:
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
        print('архів було створенно')
    except shutil.ReadError:
        print('архів не було створенно')
        folder_for_file.rmdir()
        return None
    filename.unlink()

def handle_folder(folder: Path) -> None:
    try:
        folder.rmdir()
    except OSError:
        print(f'Sorry, we can not delete the folder: {folder}')

def main(folder: Path) -> None:
    parser.scan(folder)
    for file in parser.constants.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in parser.constants.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in parser.constants.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser.constants.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')

    for file in parser.constants.AMR_AUDIO:
        handle_media(file, folder / 'audio' / 'AMR')
    for file in parser.constants.WAV_AUDIO:
        handle_media(file, folder / 'audio' / 'WAV')
    for file in parser.constants.OGG_AUDIO:
        handle_media(file, folder / 'audio' / 'OGG')
    for file in parser.constants.MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')

    for file in parser.constants.AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI')
    for file in parser.constants.MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV')
    for file in parser.constants.MOV_VIDEO:
        handle_media(file, folder / 'video' / 'MOV')
    for file in parser.constants.MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4')

    for file in parser.constants.DOC_DOCS:
        handle_media(file, folder / 'documents' / 'DOC')
    for file in parser.constants.DOCX_DOCS:
        handle_media(file, folder / 'documents' / 'DOCX')
    for file in parser.constants.PDF_DOCS:
        handle_media(file, folder / 'documents' / 'PDF')
    for file in parser.constants.TXT_DOCS:
        handle_media(file, folder / 'documents' / 'TXT')
    for file in parser.constants.PPTX_DOCS:
        handle_media(file, folder / 'documents' / 'PPTX')
    for file in parser.constants.XLSX_DOCS:
        handle_media(file, folder / 'documents' / 'XLSX')

    for file in parser.constants.GZ_ARCHIVES:
        handle_arhive(file, folder / 'archives' / 'GZ')
    for file in parser.constants.ZIP_ARCHIVES:
        handle_arhive(file, folder / 'archives' / 'ZIP')
    for file in parser.constants.TAR_ARCHIVES:
        handle_arhive(file, folder / 'archives' / 'TAR')

    for file in parser.constants.MY_OTHER:
        handle_media(file, folder / 'other')

    for folder in parser.constants.FOLDERS[::-1]:
        handle_folder(folder)

if __name__ == '__main__':
    folder_for_scan = Path(sys.argv[1])
    main(folder_for_scan.resolve())