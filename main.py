import shutil
import os

paths = []
playlistpath = input("Enter the full path to the playlist:\n")
copyto = input("Where do you want the files:\n")

try:
    os.mkdir(copyto)
except FileExistsError:
    print("Directory ", copyto, " already exists")

file = open(playlistpath, "r")
lines = file.readlines()
for line in lines:
    if line.startswith("\\"):
        paths.append(playlistpath[:2]+line[:-1])
for srcpath in paths:
    filename = os.path.basename(srcpath)
    shutil.copyfile(srcpath, copyto+filename)
    print(srcpath, " copied to ", copyto)
