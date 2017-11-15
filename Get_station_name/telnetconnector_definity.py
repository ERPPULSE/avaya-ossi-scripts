#!/usr/bin/python
# -*- coding: utf-8 -*-
# python v.3

import telnetlib, os
from configparser import ConfigParser
from time import sleep

def connector(co):
    comm = 'c' + str(co) + '\r\n'
    tn = telnetlib.Telnet(host, '5022', 10)
    tn.read_until('Login:'.encode())
    tn.write((login + '\r\n').encode())
    sleep(0.2)
    tn.read_until('Password:'.encode())
    tn.write((password + '\r\n').encode())
    tn.read_until('Terminal'.encode())
    tn.write('ossi\r\n'.encode())
    tn.read_until('t\n'.encode())
    tn.write(comm.encode())
    tn.write('t\r\n'.encode())
    output = tn.read_until('t\n'.encode())
    tn.write('clogoff\n'.encode())
    tn.write('t\n'.encode())
    sleep(0.2)
    tn.write('y\n'.encode())
    return output.decode('utf-8')

config = ConfigParser()
config.read('conf.ini')
host = config.get('Definity', 'host')
login = config.get('Definity', 'login')
password = config.get('Definity', 'password')
output = connector('list sta 2000 count 100')
filename = 'name.txt'
if os.path.isfile(filename) and os.path.getsize(filename) > 0:
    os.remove(filename)
with open('names.txt', 'a') as f:
    for i in output.split('\nn')[1:]:
        f.write('Number - {}, Name - {}\n'.format(i.split('\t')[0][2:], i.split('\t')[2]))
    f.close()
