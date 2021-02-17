import os


def delete_dup():
    dirlist = ['./Images', './Videos', './Documents',
               './Archives', './Diskimages', './Audio', './Apps']

    try:
        os.mkdir("Misc") 
    except FileExistsError:
         pass 

    for root, dir, files in os.walk('./Images', topdown=True):
        for dir2 in dir:
            dirpath = os.path.join(root, dir2)
            dirlist.append(dirpath)
#            print(dirlist)
            
    for root, dir, files in os.walk('.', topdown=True):
        dir[:] = [di for di in dir if di not in dirlist]
        print(dir)
        for file in files:
            filepath = os.path.join(root, file) 
            for d in dirlist:
                contents = os.listdir(d)
#                print(contents)
                if file in contents:
#                    print(file)
                    print(f"{file} deleted.")
                    try:
                        os.remove(f"./{file}")
                    except FileNotFoundError:
                        pass
                else:
                    try:
                        newfile = "./Misc/" + (f"{file}")
                        os.rename(filepath, newfile)
                    except FileNotFoundError:
                        pass

delete_dup()

