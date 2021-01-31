import json
import os

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
       for k in dict.keys():
         for v in  dict.values():
             for cdate in dict.keys():
               print(dict['Date'])