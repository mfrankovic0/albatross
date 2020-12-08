# albatross
My first attempt at an original script written in Python, a file organizer.

I have about a terabyte of data from an old storage drive that is extremely disorganized. I am going to seperate the script into two parts. First, I will use Python to create a list of all files sorted by their file extensions via grep and then create a central JSON file containing the list and several other pieces of information along with each item such as dates, and filepaths. Second, the script will then create the respective folders for each type of file and move all files accordingly, probably using rsync, followed by a cleanup of all old directories.  
