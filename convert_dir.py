#!/usr/bin/python
import sys

from shared import convert_dir

required_args = 1

print(len(sys.argv))
if len(sys.argv) == required_args + 1:
    expected_extension = "." + sys.argv[1]
    convert_dir(".", expected_extension, "")
else:
    print("wrong number of arguments!")
    print("expected: " + str(required_args) + ", received: " + str(len(sys.argv) - 1))
