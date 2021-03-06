# this is for settings to be used by tasks.py
import os
from os import path

###############################
# THESE SETTINGS MUST BE EDITED
###############################

# This is the directory inside the project dev dir that contains the django
# application
project_name = "wsgi-pypi"

# The django apps that are part of this project - used for running tests
# and migrations
django_apps = []

# repository type can be "cvs", "svn" or "git"
#repo_type = "svn"
#repository = 'https://svn.aptivate.org/svn/' + project_name + '/dev'

repo_type = "git"
repository = 'git://github.com/aptivate/wsgi-pypi.git'
#repository = 'git@github.com:aptivate/' + project_name + '.git'

##################################################################
# THESE SETTINGS MAY WELL BE CORRECT FOR A STANDARD DJANGO PROJECT
# BUT SHOULD STILL BE REVIEWED
##################################################################

# put "django" here if you want django specific stuff to run
# put "plain" here for a basic apache app
project_type = "plain"

# does this virtualenv for python packages
use_virtualenv = True

################################
# PATHS TO IMPORTANT DIRECTORIES
################################

# set the deploy directory to be the one containing this file
local_deploy_dir = path.dirname(__file__)

local_vcs_root = path.abspath(path.join(local_deploy_dir, os.pardir))

# the path from the VCS root to the django root dir
#relative_django_dir = path.join('django', project_name)
relative_django_dir = path.join('django', 'website')

# the directory the settings live in, relative to the vcs root
#relative_django_settings_dir = path.join(relative_django_dir, project_name)
relative_django_settings_dir = relative_django_dir

# the path from the VCS root to the virtualenv dir
relative_ve_dir = 'virtualenv'

# requirements can be in a single file, or in a directory
# the requirements file
requirements_per_env = False
local_requirements_file = path.join(local_deploy_dir, 'pip_packages.txt')

# the requirements directory
#requirements_per_env = True
#local_requirements_dir = path.join(local_deploy_dir, 'requirements')
# and the files should be path.join(requirements_dir, '%s.txt' % environment)

test_cmd = ' manage.py test -v0 ' + ' '.join(django_apps)

# servers, for use by fabric

# production server - if commented out then the production task will abort
host_list = {
    'fen-vz-pypicache': ['fen-vz-pypicache.fen.aptivate.org'],
}

# this is the default git branch to use on each server
default_branch = {
    'fen-vz-pypicache':   'master',
}

# where on the server the django apps are deployed
server_home = '/var/django'

# the top level directory on the server
# underneath it there will be dev/ containing the live instance
# and previous/ containing old copies for rollback
server_project_home = path.join(server_home, project_name)

# which web server to use (or None)
webserver = 'apache'

###################################################
# OPTIONAL SETTINGS FOR FABRIC - will be put in env
###################################################

# if you have an ssh key and particular user you need to use
# then uncomment the next 2 lines
#user = "root"
#key_filename = ["/home/shared/keypair.rsa"]
