from py2exe.build_exe import py2exe 
from distutils.core import setup

setup(
        console=['gui.py'],
        options={
                "py2exe":{
                        "includes"    : ['youtube_dl', 'PySide.QtXml']
                }
        }
)
