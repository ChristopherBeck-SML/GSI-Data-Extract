import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger','pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl','Tkconstants', 'Tkinter'],
    "zip_include_packages": ["encodings", "PySide6"],
    "optimize": 1,
    "include_files": ["README.md","install.cmd"]
}

target = Executable(
    script="extract_data.py",
    base="Win32GUI",
    icon="ico.ico"
)

setup(
    name="GSI Data Extract",
    author="Christopher Beck",
    version="0.2.1",
    options={"build_exe": build_exe_options},
    executables=[(target)]
)