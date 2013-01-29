from fabric.api import *
from fabric.contrib.project import rsync_project


env.hosts = ['prettywe@184.173.221.24:2222']


@task
def deploy():
    rsync_project(local_dir='_site/', remote_dir='public_html/trufflehub.com/')
