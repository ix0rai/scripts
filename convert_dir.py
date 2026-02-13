#!/usr/bin/python
import os
import re
import subprocess
import sys

def run_command(args: list[str]) -> None:
    subprocess.run(
        args,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

required_args = 1

print(len(sys.argv))
if len(sys.argv) == required_args + 1:
    expected_extension = "." + sys.argv[1]

    for file in os.listdir("."):
        if not file.endswith(expected_extension):
            new_file_name = re.search("[^.]*", file).group(0) + expected_extension

            print("converting: " + file)
            run_command(["ffmpeg", "-i", file, new_file_name])
            os.remove(file)
        else:
            print("no conversion required for: " + file)
else:
    print("wrong number of arguments!")
    print("expected: " + str(required_args) + ", received: " + str(len(sys.argv) - 1))