#!/bin/bash

module load anaconda
rcac-conda-env create -n POL300 -j -y
module load use.own
module load conda-env/POL300-py3.6.4
pip install textblob textstat summa pandas plotly requests bs4 lxml
echo -e "\nDone!  You can now close this tab and return to your Jupyter notebook.  Make sure you refresh the Jupyter page so the POL 300 Python environment shows up."
