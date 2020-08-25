#!/bin/bash

rcac-conda-env create -n POL300 -j -y
module load use.own
module load conda-env/POL300-py3.7.0
pip install textblob textstat summa pandas plotly requests bs4 -y
conda list -n POL300