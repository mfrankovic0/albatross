import os


def delete_dup():
    dirlist = ['./Images', './Videos', './Documents',
               './Archives', './Diskimages', './Audio', './Apps']
    
    for root, dir, files in os.walk('./Images', topdown=True):
        for dir2 in dir:
            dirpath = os.path.join(root, dir2)
            dirlist.append(dirpath)
            print(dirlist)


    for root, dir, files in os.walk('.', topdown=True):
        
        for file in files:
            for d in dirlist:
                contents = os.listdir(d)
                print(contents)
                if file in contents:
                    print(file)
                    filepath = os.path.join(root, file)
                    print(f"{file} deleted.")
                    os.remove(f"./{file}")


delete_dup()
