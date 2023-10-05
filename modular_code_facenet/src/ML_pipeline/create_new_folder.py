import os
import errno

#function to create new folder given a path 
def create_new_folder(path):
    try:
        #making a new folder
       os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise