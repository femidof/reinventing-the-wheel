#!/usr/bin/python3

import paramiko


def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
