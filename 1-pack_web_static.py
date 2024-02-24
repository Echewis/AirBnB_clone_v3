#!/usr/bin/python3
"""
This is a module  that provides a function to create a
.tgz archive from web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    # obtain the current date and time
    timenow = datetime.timenow().strftime("%Y%m%d%H%M%S")

    # Construct path where archive will be saved
    myarchive_path = "versions/web_static_{}.tgz".format(timenow)

    # use fabric function to create directory if it doesn't exist
    local("mkdir -p versions")

    # Use tar command to create a compresses archive
    archived = local("tar -cvzf {} web_static".format(myarchive_path))

    # Check archive Creation Status
    if archived.return_code != 0:
        return None
    else:
        return myarchive_path
