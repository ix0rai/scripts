#!/usr/bin/python
import sys
import os
import threading
from contextlib import chdir
import time
from typing import Callable

from shared import convert_dir, run_command

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
    global count
    thread = threading.Thread(target=lambda: animate(text), daemon=True)
    thread.start()
    process()
    time.sleep(speed)
    count = -999
    sys.stdout.write(reverser + "\n")
    sys.stdout.flush()

required_args = 3
music_path = "/media/music"
expected_extension = ".m4a"

if len(sys.argv) == required_args + 1:
    path = music_path + "/" + sys.argv[1] + "/" + sys.argv[2]
    os.makedirs(path, exist_ok=True)

    with chdir(path):
        start_animation("downloading", lambda: run_command(["yt-dlp", "-x", "--cookies-from-browser", "firefox", "--remote-components", "ejs:github", sys.argv[3]]))

        print("downloaded " + str(len(os.listdir("."))) + " songs!")

        convert_dir(".", expected_extension, "\t")

        print("success! results:", end="")
        print("", *os.listdir("."), sep="\n\t")
else:
    print("wrong number of arguments!")
    print("expected: " + str(required_args) + ", received: " + str(len(sys.argv) - 1))
