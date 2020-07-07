import sys
from cx_Freeze import setup, Executable

setup(
    name="Stepyno",
    version="1.0",
    description = "SteganoGrapy tool",
    author = "Myoung Jin Oh",
    executables = [Executable("mainwindow.py")])
