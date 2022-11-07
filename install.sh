#!/usr/bin/bash

chmod +x generator.py

mkdir -p ~/.bin >/dev/null 2>&1

mkdir -p ~/.local/share/cmaker/ >/dev/null 2>&1

cp -r templates ~/.local/share/cmaker/

cp generator.py ~/.bin/cmaker
