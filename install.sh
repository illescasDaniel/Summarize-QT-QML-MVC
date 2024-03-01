#!/bin/sh

# Detect OS platform
UNAME=$(uname | tr "[:upper:]" "[:lower:]")

# Linux
if [ "$UNAME" = "linux" ]; then
	conda env create -f environment.yml
# macOS
elif [ "$UNAME" = "darwin" ]; then
	conda env create -f environment_macOS.yml
# BSD
elif [ "$UNAME" = "freebsd" ] || [ "$UNAME" = "netbsd" ] || [ "$UNAME" = "openbsd" ]; then
	echo 'TODO?'
else
	echo 'Windows? TODO'
fi
