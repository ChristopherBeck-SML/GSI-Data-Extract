import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["encodings", "PySide6"],
    "optimize": 1,
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