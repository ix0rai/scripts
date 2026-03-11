import subprocess
import os
import re

def run_command(args: list[str]) -> None:
    subprocess.run(
        args,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def convert_dir(path: str, extension: str, indent: str) -> None:
    for file in os.listdir(path):
        if not file.endswith(extension):
            converted_file_name = re.search("[^.]*", file).group(0) + extension

            print(indent + "converting: " + file)
            run_command(["ffmpeg", "-i", file, converted_file_name])
            os.remove(file)
        else:
            print(indent + "no conversion required for: " + file)
    return