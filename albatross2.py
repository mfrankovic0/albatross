import json
import os
from datetime import datetime

"""move_files() opens the JSON files and moves the files within to their 
   respective folders.
"""

types = ['Images', 'Videos', 'Documents',
         'Archives', 'Diskimages', 'Audio', 'Apps']

for type0 in types:
    jsonfile = open(f'{type0}.json')
    dict = json.load(jsonfile)
    dir = f"./{type0}"
    os.mkdir(dir)
    if type0 == 'Images':
        for v in dict.values():
            subdir = f"./{type0}/{v['Date']}"
            try:
                os.mkdir(subdir)
            except FileExistsError:
                pass
            move = f"mv {v['Path']} {subdir}"
            os.system(move)
    else:
       