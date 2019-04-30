#https://stackoverflow.com/questions/37912867/renaming-a-single-file-in-python
import os

#src = "D:/test/Untitled003.wav"
#dst = "D:/test/Audio001.wav"
src = "/home/mthomas/Downloads/baabaa baa.txt"
dst = "/home/mthomas/Downloads/bubbafool46.txt"
if os.path.isfile(src):
    os.rename(src, dst)