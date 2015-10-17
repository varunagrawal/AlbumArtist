import os
import json

with open("music_filetypes.json", 'r') as f:
    ftypes = json.loads(f.read())

valid_exts = [type["extension"] for type in ftypes["filetypes"]]


def get_all_music_files(musicdir):
    music = []

    for root, subdir, filelist in os.walk(musicdir):
        #print("PWD: {0}".format(directory))
        #print("This directory has:")
        for file in filelist:
            if file.split('.')[-1] in valid_exts:
                #print("\t {0}".format(os.path.join(root, file)))
                music.append(os.path.join(root, file))

        #print("\n")

    return music

if __name__ == "__main__":
    print(valid_exts)
    musicdir = "/Users/varun/Music/"
    music = get_all_music_files(musicdir)
