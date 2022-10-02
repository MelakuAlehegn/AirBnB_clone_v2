#!/usr/bin/python3

"""
a Fabric script that generates a .tgz archive from the
contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""


import tarfile
from datetime import datetime
from fabric.api import local


def do_pack():
    '''
    a function that generates a tar file from a directory
    '''

    now = datetime.now()
    nowt = now.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    file_name = "versions/{}{}.tgz".format('web_static_', nowt)
    print(file_name)
    command = local("tar -cvzf {} web_static".format(file_name))
    if command.succeeded:
        return file_name
    else:
        return None
