import os
import json
import datetime

txtlist = {}

def find_txt():
    for root, dirs, files in os.walk("/home/mike/Downloads/Tool/"):
        for file in files:
            if file.endswith((".flac", ".ape", ".mp3, ")):
                filename, file_extension = os.path.splitext(file)
                pathname = os.path.join(root, file)
                try:
                    cdate = os.stat(file).st_ctime
                    date = datetime.fromtimestamp(cdate)
                except FileNotFoundError:
                    continue 
                txtlist.update({filename: {'Path': pathname, 'files_ext': file_extension, 'date': date}})

find_txt()

with open('test.json', 'w') as json_file:
    json.dump(txtlist, json_file, sort_keys=True, indent=4)