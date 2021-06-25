# -*- coding: utf-8 -*-
"""


"""

from netmiko import ConnectHandler

vyos = {
    'device_type': 'vyos',
    'ip':   '10.10.10.1',
    'username': 'vyos',
    'password': 'vyos',
#   'port' : 8022,          # optional, defaults to 22
#   'secret': 'secret',     # optional, defaults to ''
#   'verbose': False,       # optional, defaults to False
}
net_connect = ConnectHandler(**vyos)
output = net_connect.send_command('show configuration')
print(output)

