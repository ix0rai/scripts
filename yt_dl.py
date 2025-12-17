#!/usr/bin/python
import subprocess
import sys
import os
import re
import threading
from contextlib import chdir
import time
from typing import Callable

animation = ("   ", ".  ", ".. ", "...") # all strings must have the same number of chars!

speed = 0.5
reverser = ''.join('\b' * len(animation[0]))
count = 0

def animate(text: str) -> None:
    global count
    count = 0
    sys.stdout.write(text)
    while True:
        if count < 0:
            break
        if count != 0:
            sys.stdout.write(reverser)

        sys.stdout.write(animation[count % len(animation)])
        sys.stdout.flush()
        time.sleep(speed)
        count += 1

def start_animation(text: str, process: Callable[[], None]) -> None:
    thread = threading.Thread(target=lambda: animate(text), daemon=True)
    thread.start()
    process()
    global count
    time.sleep(speed)
    count = -1
    sys.stdout.write(reverser + "\n")
    sys.stdout.flush()

def run_command(args: list[str]) -> None:
    subprocess.run(
        args,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

required_args = 3
music_path = "/media/music"
expected_extension = ".m4a"

if len(sys.argv) == required_args + 1:
    path = music_path + "/" + sys.argv[1] + "/" + sys.argv[2]
    os.makedirs(path, exist_ok=True)

    with chdir(path):
        start_animation("downloading", lambda: run_command(["yt-dlp", "-x", "--cookies-from-browser", "firefox", sys.argv[3]]))
        print("finished download!")

        files = os.listdir(".")

        for file in files:
            if not file.endswith(expected_extension):
                new_file_name = re.search("[^.]*", file).group(0) + expected_extension

                print("converting: " + file)
                run_command(["ffmpeg", "-i", file, new_file_name])

                print("removing: " + file)
                os.remove(file)
            else:
                print("no conversion required for: " + file)

        print("success! downloaded:", end="")
        print("", *files, sep="\n\t")
else:
    print("wrong number of arguments!")
    print("expected: " + str(required_args) + ", received: " + str(len(sys.argv) - 1))
