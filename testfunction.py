import os
import json

def find_txt():
    for root, dirs, files in os.walk(".txt", topdown=False):
        print(os.path.join(files, name))

find_txt()