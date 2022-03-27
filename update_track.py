#!/usr/bin/python
import os, sys
import wget

def get_best_track():
    url = 'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt'
#url = 'https://trackerslist.com/best.txt'
    name = wget.download(url)
    return name 

def make_tracks(track_file):
    tracks = 'bt-tracker='
    with open(track_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if len(line) > 1:
                tracks += (line[:-1] + ',');
    os.remove(track_file)
    tracks = tracks[:-1]
    print(tracks)
    return tracks

def update_track(conf_file, tracks):
    lines = []
    with open(conf_file, 'r') as f:
        lines = f.readlines()
        lines = lines[:-1]
    with open(conf_file, 'w') as f:
        lines.append(tracks)
        f.writelines(lines)

def main(conf_file):
    track_file = get_best_track()
    tracks = make_tracks(track_file)
    update_track(conf_file, tracks)

if __name__ == "__main__":
    main('aria2.conf')
