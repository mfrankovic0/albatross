import json

"""
mydict = {   
   'items': [
       {
           'id': '12345',
           'links': {'self': 'https://www.google.com'},
           'name': 'beast',
           'type': 'Device'
       }
    ],
    'links': {'self': 'https://www.google.com'},
    'paging': {
        'count': 1,
        'limit': 1,
        'offset': 0,
        'pages': 1
    }
}

print(mydict['items'][0]['id'])
print(mydict['items'][0]['links']['self'])
print(mydict['links']['self'])
print(mydict['items'][0]['name'])
"""

filelist = { 
    "filename":
        {
          "path": "filepath",
          "date": "date",
          "file_ext": "file extension"
        }
}

with open('test.json', 'w') as json_file:
  json.dump(filelist, json_file, sort_keys=True, indent=4)
