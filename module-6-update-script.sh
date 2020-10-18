  
#!/bin/bash

module load anaconda
module load use.own
module load conda-env/POL300-py3.6.4
pip install nbformat --upgrade

echo "c.NotebookApp.iopub_data_rate_limit = 1e10" >>.jupyter/jupyter_notebook_config.py

echo -e "\nDone!  You can now close this tab and return to your Jupyter notebook.  Make sure you refresh the Jupyter page!"
