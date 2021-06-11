import pathlib
from setuptools import setup

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
    ],   
    version = '0.0.9',      # Start with a small number and increase it with every change you make
    license="GNU General Public License v3.0",        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Custom widgets and widget animations made for QT applications',   # Give a short description about your library
    long_description=README,
    long_description_content_type="text/markdown",
    author = 'Khamisi Kibet',                   # Type in your name
    author_email = 'kibetkhamisi@gmail.com',      # Type in your E-Mail
    url = 'https://github.com/KhamisiKibet/QT-PyQt-PySide-Custom-Widgets',   # Provide either the link to your github or to your website
    # download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
    keywords = ['PySide', 'PyQt', 'animation', 'custom', 'widgets'],   # Keywords that define your package best
    install_requires=[
        "PySide2",
        "PyQt5",
        "iconify",
    ],
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
