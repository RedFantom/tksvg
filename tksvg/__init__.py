"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2021 RedFantom
"""
import contextlib
import tkinter as tk
import os


@contextlib.contextmanager
def chdir(target: str):
    """Context-managed chdir, original implementation by GitHub @Akuli"""
    current = os.getcwd()
    try:
        os.chdir(target)
        yield
    finally:
        os.chdir(current)

def load(window: tk.Tk):
    """Load tksvg into a Tk interpreter"""
    local = os.path.abspath(os.path.dirname(__file__))
    with chdir(local):
        window.tk.eval("source pkgIndex.tcl")
        window.tk.eval("package require tksvg")
