#! /usr/bin/python3

"""This script serves as a simple way of downloading external data files needed for packing a self-contained wheel"""
from pathlib import Path
from urllib import request


DATA_FILES = {
    'https://raw.githubusercontent.com/antlr/grammars-v4/master/vba/vba.g4': None,
    'https://www.antlr.org/download/antlr-4.9.2-complete.jar': None,
}

for netloc, local_filepath in DATA_FILES.items():
    local_filepath = Path(local_filepath or Path('data') / Path(netloc).name)
    if local_filepath.exists():
        print('Data file "{netloc}" already downloaded to "{local_filepath}"'.format(**locals()))
    else:
        print('Downloading data file "{netloc}" -> "{local_filepath}"'.format(**locals()))
        local_filepath.parent.mkdir(parents=True, exist_ok=True)
        request.urlretrieve(netloc, str(local_filepath))
