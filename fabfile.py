# coding: utf-8

import os
import sys
from contextlib import contextmanager
from distutils.util import strtobool

from fabric.api import cd, env, local, parallel, prefix, put, run, sudo, task
from fabric.colors import green, magenta, yellow, red
from fabric.context_managers import shell_env



DEFAULTS = {
    'user': 'vericant',
    'git_path': '/opt/git/vericant-prototyping.git',
    'git_branch': 'develop',
    'django_settings_module': 'settings.local',
    'django_configuration': 'Local',
    'deploy_path': '/opt/vericant-prototyping',
    'dist_path': 'dist',
    'virtualenv': '/opt/virtualenvs/vericant',
    'requirements': 'production.txt',
    'server': 'development'
}

SERVERS = {
    'prototyping': {
        'host': 'proto.vcnt.co',
        'configuration': 'develop'
    },
}

env.roledefs = {
    'production': [

    ],
    'development': [
        SERVERS['prototyping'],
    ],
}



@task
def deploy(branch=None, server=None):
    git_branch = branch or _get_conf('git_branch')
    server = server or _get_conf('server')
    user = _get_conf('user')
    git_path = _get_conf('git_path')
    deploy_path = _get_conf('deploy_path')
    dist_path = _get_conf('dist_path')
    requirements = _get_conf('requirements')

    print magenta('Deploying branch {} to {}...'.format(git_branch, env.host))

    # Local Build of Distribution items
    _local_build()

    # Deploy locally build Distribution to remote
    _remote_upload(_env(server), deploy_path, dist_path)

    print green('Deployed OK.')

def _env(server):
    return 'proto.vcnt.co'

def _local_build():
    print magenta('Running NPM install and post-install scripts')
    local('yarn install')

def _remote_upload(host, remote_path, local_path):
    _clear_remote(host, remote_path)
    print magenta('Deploying Compilation to {}...'.format(host), bold=True)
    local('scp -r {}/* {}:{}'
        .format(local_path, host, remote_path))

def _clear_remote(host, remote_path):
    print magenta('Cleaning Remote Path')
    local('ssh {} "rm -fr {}/*"'
        .format(host, remote_path))

def _get_conf(key, host=None):
    host_string = host if host else env.host_string
    conf_dict = _get_conf_dict(host_string)
    return conf_dict.get(key)

def _get_conf_dict(host):
    hosts = {SERVERS[k]['host']: SERVERS[k] for k in SERVERS}
    if host in hosts:
        return dict(DEFAULTS.items() + hosts[host].items())
    else:
        return DEFAULTS
