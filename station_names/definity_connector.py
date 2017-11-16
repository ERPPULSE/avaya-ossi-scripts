#!/usr/bin/python
# -*- coding: utf-8 -*-

import telnetlib
from configparser import ConfigParser
from time import sleep

def connector(co):
    '''Функція приймає команду станції як аргумент і видає
результат на введену команду'''
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

def paramset(command, field, param):
    if command[:2] == 'ch':
        tn = telnetlib.Telnet(host, '5022', 10)
        tn.read_until('Login'.encode())
        tn.write((login + '\r\n').encode())
        sleep(0.2)
        tn.read_until('Password'.encode())
        tn.write((password + '\r\n').encode())
        tn.read_until('Terminal'.encode())
        tn.write('ossi\r\n'.encode())
        tn.read_until('t\n'.encode())
        tn.write(('c' + str(command) + '\n').encode())
        tn.write((str(field) + '\n').encode())
        tn.write(('d' + str(param) + '\n').encode())
        tn.write('t\n'.encode())
        tn.write('clogoff\n'.encode())
        tn.write('t\n'.encode())
        sleep(0.2)
        tn.write('y\n'.encode())
    else:
        print('Error in first function parameter')

config = ConfigParser()
config.read('conf.ini')
host = config.get('Definity', 'host')
login = config.get('Definity', 'login')
password = config.get('Definity', 'password')
	
