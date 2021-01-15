import os
import json
from datetime import date


txtlist = {}

def find_txt():
    for root, dirs, files in os.walk("/home/mike/Programming/albatross"):
        for file in files:
            if file.endswith((".txt")):
                filename, file_extension = os.path.splitext(file)
                pathname = os.path.join(root, file)
                try:
                    cdate = os.stat(file).st_ctime
                    datee = date.fromtimestamp(cdate)
                except FileNotFoundError:
                    continue 
                txtlist.update({filename: {'Path': pathname, 'files_ext': file_extension, 'date': datee}})

find_txt()

with open('test.json', 'w') as json_file:
    json.dump(txtlist, json_file, sort_keys=True, indent=4)