#!/usr/bin/env bash
python -m pip install --upgrade pipenv
pipenv install 
pipenv run python freeze.py