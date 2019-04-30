#https://stackoverflow.com/questions/8933237/how-to-find-if-directory-exists-in-python
import os

fuddit = (os.path.isdir("/var/log/updates/protex/foo"))

if fuddit==True:
    print("directory exists")
else:
    print("directory not found")