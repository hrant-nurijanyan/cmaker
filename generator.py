#!/usr/bin/python3

import argparse
import os
from pathlib import Path
import shutil

parser = argparse.ArgumentParser(
    description="Generate C++ CMakeProject based on arguments provided")
parser.add_argument('name', help="Name of the project")
parser.add_argument('-s', '--standard',
                    help="C++ standard of the project", type=str)
parser.add_argument('-cv', '--cmake_version',
                    help="Version of the cmake", type=str)
parser.add_argument('-t', '--template', help="Project template", type=str)
parser.add_argument(
    '-l', '--lib', help="If provided a static library cmake is generated", action='store_true')

standards = ['03', '11', '14', '17', '20', '23']
templates = ['clean']

args = parser.parse_args()

if args.standard is not None:
    if args.standard not in standards:
        raise ValueError(
            f'Invalid standard only {standards} are supported but current value is {args.standard}')
else:
    args.standard = '17'  # defaulting to 17 standard of C++

if args.template is not None:
    if args.template not in templates:
        raise ValueError(
            f'Invalid project template type, it must be one of {templates} but is {args.template}')
else:
    args.template = 'clean'

name = args.name
isLib = args.lib
standard = args.standard
cmake_version = args.cmake_version or '3.22.1'  # defaulting to cmake 3.22.1
template = args.template

# Removing project directory if exists
if os.path.exists(name):
    shutil.rmtree(name)

# Getting project template dir
template_dir = str(Path('~').expanduser()) + \
    f"/.local/share/cmaker/templates/cpp_{template}"

# Copying template to the project root dir
shutil.copytree(os.path.abspath(template_dir), name)

os.chdir(name)


# Reading content of CMakeLists
content = None
with open('CMakeLists.txt', 'r') as CMakeLists:
    content = CMakeLists.read()
    content = content.replace(
        "{min_cmake_version}", f'VERSION {cmake_version}')
    content = content.replace("{project_name}", name)
    content = content.replace("{cxx_standard}", standard)
    content = content.replace("{project_type}", "library") if isLib else content.replace(
        "{project_type}", "executable")

if content is None:
    raise ValueError("Invalid CMakeLists.txt")

with open('CMakeLists.txt', 'w') as CMakeLists:
    CMakeLists.write(content)
