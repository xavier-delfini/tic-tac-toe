import glob, os
os.chdir("players/")
for file in glob.glob("*.json"):
    print(file[:-5])