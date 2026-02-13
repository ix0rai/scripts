#!/usr/bin/python
import os
import re
import subprocess
import shutil

def run_command(args: list[str]) -> None:
    subprocess.run(
        args,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

output = os.path.join(os.getcwd(), "output")
stripped_path = "/media/music/"

print("copying " + stripped_path)
if os.path.isdir(output):
    shutil.rmtree(output)
subprocess.call(["cp", "-r", stripped_path, output])

files = os.listdir(output)

for artist in files:
    artist_path = os.path.join(output, artist)
    if artist.startswith(".") or not os.path.isdir(artist_path):
        continue

    print(artist)
    for album in os.listdir(artist_path):
        album_path = os.path.join(artist_path, album)

        print("\t" + album)

        cover_path = os.path.join(album_path, "cover.jpg")

        # todo add progress indicator
        for file in os.listdir(album_path):
            if not file.endswith(".mp3"):
                file_path = os.path.join(album_path, file)
                new_file_name = re.search("[^.]*", file).group(0) + ".mp3"
                temp_file_name = re.search("[^.]*", file).group(0) + ".temp.mp3"
                temp_meta_file_name = re.search("[^.]*", file).group(0) + ".temp.meta.txt"
                new_file_path = os.path.join(album_path, new_file_name)
                temp_file_path = os.path.join(album_path, temp_file_name)
                temp_meta_file_path = os.path.join(album_path, temp_meta_file_name)


                # fetch cover from first file
                if not os.path.isfile(cover_path):
                    print("\t\textracting cover")
                    run_command(["ffmpeg", "-i", file_path, "-vf", "scale=250:250", cover_path])
                    # todo probably lots of redundant metadata in here
                    run_command(["exiftool",
                                 "-overwrite_original",
                                 "-ResolutionUnit=inches",
                                 "-ExifVersion=0232",
                                 "-ComponentsConfiguration=Y,Cb,Cr,-",
                                 "-ColorSpace=Uncalibrated",
                                 "-ExifImageWidth=250",
                                 "-ExifImageHeight=250",
                                 cover_path,
                                 ])

                # convert and remove
                print("\t\tconverting: " + file + " -> " + new_file_name)

                # todo name file based on title?
                # get title
                # run_command([
                #     "ffmpeg",
                #     "-i", file_path,
                #     "-f", "ffmetadata",
                #     temp_meta_file_path
                # ])

                # title = "not found"
                # with open(temp_meta_file_path) as f:
                #     for line in f:
                #         if line.startswith("title"):
                #             title = line.split("=")[1].strip()


                run_command(["ffmpeg",
                             "-i", file_path,
                             "-id3v2_version", "3",
                             temp_file_path])

                run_command(["ffmpeg",
                             "-i", temp_file_path,
                             "-i", cover_path,
                             "-map", "0:0",
                             "-map", "1:0",
                             "-c", "copy",
                             "-id3v2_version", "3",
                             "-metadata:s:v", "title=\"Album cover\"",
                             "-metadata:s:v", "comment=\"Cover (front)\"",
                             new_file_path])
                os.remove(file_path)
                os.remove(temp_file_path)
            else:
                print("no conversion required for: " + file)