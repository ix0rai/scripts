#!/usr/bin/python
import os
from contextlib import chdir

path = "/media/music/"

artists: dict[str, dict[str, int]] = {}
playlists = 0

most_tracks_name = ""


with chdir(path):
    files = os.listdir(".")
    for artist in files:
        if artist.startswith("."):
            continue

        if not os.path.isdir(artist) and artist.endswith(".m3u"):
            playlists += 1
            continue

        artists[artist] = {}

        for album in os.listdir(artist):
            artists[artist][album] = 0
            for track in os.listdir(os.path.join(artist, album)):
                artists[artist][album] += 1

total_artists: int = len(artists)
total_albums: int = sum(len(d) for d in artists.values())
total_tracks: int = sum(sum(d.values()) for d in artists.values())

print("artists:\t" + str(total_artists))
print("albums:\t\t" + str(total_albums))
print("tracks:\t\t" + str(total_tracks))
print("playlists:\t" + str(playlists))
print()
print("averages:"
        + "\n\taverage tracks per album:\t" + f"{total_tracks / total_albums:.2f}"
        + "\n\taverage albums per artist:\t" + f"{total_albums / total_artists:.2f}"
)