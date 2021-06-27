# -*- coding: utf-8 -*-
"""
@author: kaisar
"""


#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "device_type": "cisco_ios",
    "host": "10.10.10.11",
    "username": "admin",
    "password": 'cisco',
}

# File in same directory as script that contains
#
# $ cat config_changes.txt 
# --------------
# logging buffered 100000
# no logging console

cfg_file = "config_changes.txt"
with ConnectHandler(**device1) as net_connect:
    output = net_connect.send_config_from_file(cfg_file)
    output += net_connect.save_config()

print()
print(output)
print()
