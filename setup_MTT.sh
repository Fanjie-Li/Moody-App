#!/bin/bash

# How to run this Bash script:
# cd {filepath-of-project-folder}
# sh setup_MTT.sh


# Uncomment the following line if you haven't got the latest version of python 3 installed
# brew install python3

pip3 install -r requirements.txt

python3 multitasking_test.py