#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the
function do_deploy
"""

from fabric.api import *
import os.path
from datetime import datetime

env.hosts = ['3.236.253.64', '18.207.158.241']

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

def do_deploy(archive_path):
    '''
    a function to deploy an archive
    '''

    path = os.path.exists(archive_path)
    if path:
        file_path = archive_path.split("/")[-1]
        without_ext = file_path.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, without_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_path, path, without_ext))
        run('rm /tmp/{}'.format(file_path))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, without_ext))
        run('rm -rf {}{}/web_static'.format(path, without_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, without_ext))

        print("New version deployed!")
        return True

    return False

def deploy():
    """creates and distributes the archive to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
