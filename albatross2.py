import json
import os
from datetime import datetime

"""move_files() opens the JSON files generated by albatross.py and moves the 
   files within to their respective folders.
"""

types = ['Images', 'Videos', 'Documents',
         'Archives', 'Diskimages', 'Audio', 'Apps']


def move_files():
    for type0 in types:
        jsonfile = open(f'{type0}.json')
        dict = json.load(jsonfile)
        dir = f"./{type0}"
        try:
            os.mkdir(dir)
        except (FileExistsError):
            pass
        if type0 == 'Images':
            for v in dict.values():
                subdir = f"./{type0}/{v['Date']}"
                filename = os.path.basename(v['Path'])
                try:
                    os.mkdir(subdir)
                except FileExistsError:
                    pass
                source = str(f"{v['Path']}")
                dest = str(f"{subdir}/{filename}")
                print(source, dest)
                try:
                    os.rename(f"{source}", f"{dest}")
                except Exception as e:
                    print(e)
                    pass    
        elif type0 != 'Images':
            for v in dict.values():
                filename = os.path.basename(v['Path'])
                source2 = str(f"{v['Path']}")
                dest2 = str(f"{dir}/{filename}")
                try:
                    os.rename(f"{source}2", f"{dest2}")
                except Exception as e:
                    print(e)
                    pass         
        else:
            continue

move_files()
