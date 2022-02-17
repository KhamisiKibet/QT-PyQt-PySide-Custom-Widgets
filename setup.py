import pathlib
from setuptools import setup
import platform
import ctypes, os
import subprocess
def isAdmin(): #Credit to https://raccoon.ninja/en/dev/using-python-to-check-if-the-application-is-running-as-an-administrator/
    try:
        is_admin = (os.geteuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin #If this is not run as an admin on Windows, you will get WinError permission denied for Local/Temp folder in %appdata%.
if platform.system() == "Linux" or platform.system() == "Darwin":
    install_requires=[
        "PySide2",
        "PyQt5",
        "iconify",
        "cairosvg",
        "codecs",
        "shutil",
        "qtsass",
        "matplotlib",
        "mock",
        "urllib",
        "colorsys"
    ]
else:
    if not isAdmin():
        print("This script needs to be run as administrator.")
        exit(-1)
    from urllib.request import urlretrieve #This has to be done here, not at the top of the file because only Windows users have access to this from the STDLIB
    print("Downloading GTK installer. This is not optional. Without this installed, Custom_Widgets will fail.")
    urlretrieve("https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2022-01-04/gtk3-runtime-3.24.31-2022-01-04-ts-win64.exe", "gtk.exe")
    """Code above downloads the GTK3+ installer. Without this, cairosvg will spit out multiple errors about GTK DLLs being missing."""
    print("GTK installer downloaded. Leave all settings at default. Running now...")
    subprocess.call("gtk.exe", shell=True)
    print("GTK installed.")
    os.remove(os.getcwd()+"\\gtk.exe")
    install_requires=[
        "PySide2",
        "PyQt5",
        "iconify",
        "cairosvg",
        "qtsass",
        "matplotlib",
        "mock",
    ]
    """Python 3.9 for Windows already includes shutil, codecs, colorsys and urllib. This change will remove the error preventing
    installation on Windows devices."""
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name = 'QT-PyQt-PySide-Custom-Widgets',         # How you named your package folder (MyLib)
    packages = [
        'Custom_Widgets', 
        'Custom_Widgets.ProgressIndicator',
        'Custom_Widgets.Qss',
    ],   
    version = '0.4.1',      # Start with a small number and increase it with every change you make
    license="GNU General Public License v3.0",        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Custom widgets and widget animations made for QT applications',   # Give a short description about your library
    long_description=README,
    long_description_content_type="text/markdown",
    author = 'Khamisi Kibet',                   # Type in your name
    author_email = 'kibetkhamisi@gmail.com',      # Type in your E-Mail
    url = 'https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets',   # Provide either the link to your github or to your website
    # download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
    keywords = ['PySide', 'PyQt', 'animation', 'custom', 'widgets', "QML", "C++", "QT Creator"],   # Keywords that define your package best
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={
        
    },
)
