import os
import json
from datetime import date

"""find_file() will search through directories for files with the 
    specified file extensions for each corresponding function. The results will
    be added to a dictionary along with metadata. When it is finished, the 
    dictionaries will be dumped into a JSON file for each 
"""


FileTypes = {
    "Images": (
        ".jpeg",
        ".jpg",
        ".tiff",
        ".gif",
        ".bmp",
        ".png",
        ".bpg",
        ".svg",
        ".heif",
        ".psd",
        ".cr2",
        ".indd"
    ),
    "Videos": (
        ".avi",
        ".flv",
        ".wmv",
        ".mov",
        ".mp4",
        ".webm",
        ".vob",
        ".mng",
        ".qt",
        ".mpg",
        ".mpeg",
        ".3gp",
        ".mkv"
    ),
    "Documents": (
        ".txt",
        ".oxps",
        ".epub",
        ".pages",
        ".docx",
        ".doc",
        ".fdf",
        ".ods",
        ".odt",
        ".pwi",
        ".xsn",
        ".xps",
        ".dotx",
        ".docm",
        ".dox",
        ".rvg",
        ".rtf",
        ".rtfd",
        ".wpd",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".md",
        ".pages",
        ".numbers",
        ".pdf",
        ".json"
    ),
    "Archives": (
        ".a",
        ".ar",
        ".arh",
        ".tar",
        ".tar.bz2",
        ".tar.gz",
        ".cpio",
        ".tar",
        ".gz",
        ".rz",
        ".7z",
        ".rar",
        ".xar",
        ".zip",
        ".xz",
        ".pkg",
        ".deb",
        ".rpm"
    ),
    "Diskimages": (
        ".iso",
        ".img",
        ".vcd",
        ".dmg"
    ),
    "Audio": (
        ".flac",
        ".ape",
        ".aac",
        ".aa",
        ".aac",
        ".dvf",
        ".m4a",
        ".m4b",
        ".m4p",
        ".mp3",
        ".msv",
        ".ogg",
        ".oga",
        ".raw",
        ".vox",
        ".wav",
        ".wma"
    ),
    "Apps": (
        ".exe",
        ".msi"
    )
}


def find_file(filetype, ext):
    filelist = {}
    for root, directories, files in os.walk('.', topdown=True):
        exclude = set('Music')
        directories[:] = [d for d in directories if d not in exclude]
        for file in files:
            if file.endswith(ext):
                filename, file_ext = os.path.splitext(file)
                pathname = os.path.join(root, file)
                cdate = os.stat(pathname).st_ctime
                timestamp = date.fromtimestamp(cdate)
                fdate = timestamp.strftime("%m-%Y")
                filelist.update(
                    {filename: {'Path': pathname, 'File Extension': file_ext, 'Date': fdate}})
    filegroup = f"{filetype}.json"
    with open(filegroup, 'w') as json_file:
        json.dump(filelist, json_file, sort_keys=True, indent=4)


for k, v in FileTypes.items():
    find_file(k, v)
