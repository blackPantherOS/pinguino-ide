#!/bin/sh
#
# Launch Pinguino's IDE
echo "Launch Pinguino's IDE ..."
mkdir -p ~/Pinguino/v13/pinguino-libraries/p8/pdl
mkdir -p ~/Pinguino/v13/pinguino-libraries/p32/pdl
mkdir -p ~/Pinguino/v13/pinguino-libraries/p8/include/pinguino/core
mkdir -p ~/Pinguino/v13/pinguino-libraries/p8/include/pinguino/core
mkdir -p ~/Pinguino/v13/pinguino-libraries/p8/include/pinguino/libraries

# Optional for not packaged version
#mkdir -p ~/Pinguino/v13/pinguino-ide/
#cd ~/Pinguino/v13/pinguino-ide/
#python3 -m pip install pipenv
#python3 -m pipenv install
#python3 -m pipenv run python pinguino-ide.py
