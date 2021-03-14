#!/usr/bin/bash

# initial setup for using this repository

function setup()
{
    FILE=$HOME/.jupyter/jupyter_notebook_config.py
    if [ ! -f "$FILE" ]; then
        pipenv run jupyter notebook --generate-config
    fi

    echo 'c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"' | tee -a ~/.jupyter/jupyter_notebook_config.py
    echo 'c.ContentsManager.default_jupytext_formats = "ipynb,py"' >> ~/.jupyter/jupyter_notebook_config.py
}

function install()
{
    if [ "$1" = pipenv ]; then
        pipenv install -r requirements.txt
        setup $1
    else
        pip install -r requirements.txt
    fi

    return 0
}

install $1
