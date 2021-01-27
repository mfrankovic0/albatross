import os
import json
from datetime import date


    """
    ListGen(erator) will search through directories for files with the 
    specified file extensions for each corresponding function. The results will
    be added to a dictionary along with metadata. When it is finished, the 
    dictionaries will be dumped into a JSON file.
    """

FileTypes =
{
  "Images": [
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
  ],
  "Videos": [
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
  ],
  "Documents": [
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
    ".pdf"
  ],
  "Archives": [
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
  ],
  "Diskimages": [
    ".iso",
    ".img",
    ".vcd",
    ".dmg"
  ],
  "Audio": [
    "flac",
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
    "ogg",
    "oga",
    ".raw",
    ".vox",
    ".wav",
    ".wma"
  ],
  "Apps": [
    ".exe",
    ".msi"
  ]
}

filelist = {}

def find_file(filetype, ext):
    for root, dirs, files in os.walk("/home/mike/albatross"):
        for file in files:
            if file.endswith((".txt")):
                filename, file_ext = os.path.splitext(file)
                pathname = os.path.join(root, file)
                try:
                    cdate = os.stat(file).st_ctime
                    timestamp = date.fromtimestamp(cdate)
                    fdate = timestamp.strftime("%D")
                except FileNotFoundError:
                    continue 
                filelist.update({filename: {'Path': pathname, 'File Extension': file_ext, 'Date': fdate}})

find_file()

with open('test.json', 'w') as json_file:
    json.dump(txtlist, json_file, sort_keys=True, indent=4)