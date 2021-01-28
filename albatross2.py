import json
import os

"""move_files() opens the JSON files and moves the files within to their 
   respective folders.
"""

types = ('Images', 'Videos', 'Documents',
         'Archives', 'Diskimages', 'Audio', 'Apps')

for type in types:
    jsonfile = open(f'{type}.json')
     = json.load(jsonfile)
    print()
