"""
Image location support
"""

import fnmatch
import os
from typing import List

from kids.cache import cache

_USER_DIR = os.path.expanduser('~/.iconify')
_ICON_PATH = os.environ.get('ICONIFY_PATH', _USER_DIR).split(os.pathsep)


class IconNotFoundError(Exception):
    pass


def addIconDirectory(directoryLocation):
    # type: (str) -> None
    """
    Add the provided path to the list of directories that iconify will use
    when looking for svg files.

    Parameters
    ----------
    directoryLocation : str
    """
    _ICON_PATH.append(directoryLocation)


@cache
def findIcon(iconPath):
    # type: (str) -> str
    """
    Use the provided string to find an svg file on the iconify path.

    Any `:`'s in the provided string will be replaced with the current
    platform's directory separator.

    Parameters
    ----------
    iconPath : str

    Returns
    -------
    str
    """
    if os.path.isabs(iconPath):
        if not os.path.isfile(iconPath):
            raise IconNotFoundError(
                "Unable to locate icon file: {}".format(iconPath)
            )
        return iconPath
    else:
        iconPath = iconPath.replace(":", os.sep)
        for dir_ in _ICON_PATH:
            absIconPath = os.path.join(dir_, iconPath + ".svg")
            if os.path.isfile(absIconPath):
                return absIconPath

        raise IconNotFoundError(
            "Unable to find an icon on the ICONIFY_PATH that matches '{}'".
            format(iconPath)
        )


def listIcons():
    # type: () -> List[str]
    """
    Return all icons found on the iconify path.

    Returns
    -------
    List[str]
    """
    matches = []  # type: List[str]
    for dir_ in _ICON_PATH:
        for root, dirnames, filenames in os.walk(dir_):
            for filename in fnmatch.filter(filenames, '*.svg'):
                filePath = os.path.join(root, filename)
                filePath = filePath.replace(dir_, "")
                filePath, _ = os.path.splitext(filePath)
                filePath = filePath.lstrip(os.sep).replace(os.sep, ":")
                matches.append(str(filePath))
    return matches
