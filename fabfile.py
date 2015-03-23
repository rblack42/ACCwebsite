from fabric.api import *
import os

def setup():
    if not os.path.isdir('_venv'):
        local('virtualenv _venv')

def update_reqs():
    local('source _venv/bin/activate && pip install -r requirements.txt')

def build():
    local('sphinx-build -b html -d _build/doctrees . _build/html')
