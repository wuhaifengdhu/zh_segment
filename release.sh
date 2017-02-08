#!/bin/bash

#####################################################
#  command to create egg_info:
#              python setup.py egg_info
######################################################

# Step 1, Remove old dist files
rm -rf ./dist/*

# Step 2, Build deploy files
python setup.py sdist
python setup.py bdist_wheel --universal
twine upload dist/*
