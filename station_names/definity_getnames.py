#!/usr/bin/python
# -*- coding: utf-8 -*-
# python v.3

import telnetlib, os
from configparser import ConfigParser
from time import sleep

def translater(inputstring):
    '''функція перетворює текст введений анг. літерами на
українскі літери та робить всі перші букви слів великими'''
    eng = 'qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./'
    ua = 'йцукенгшщзхї\фівапролджєячсмитьбю.'
    trans = str.maketrans(eng, ua)
    if len(inputstring) > 0 and inputstring[0] == '~': #якщо вхідна строка більша 0 і починається з ~
        return f'{inputstring.lower().translate(trans).title()}'[1:] #перевести строку в нижній регістр перекласти побуквенно строку і всі перші слова в сроці зробити великими
    else:
        return inputstring
    
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

config = ConfigParser()
config.read('conf.ini')#файл з параметрами для входу в станцію
host = config.get('Definity', 'host')
login = config.get('Definity', 'login')
password = config.get('Definity', 'password')
output = connector('list sta 2000 count 800')#команда в станції
filename = 'name.txt'#вихідний файл
if os.path.isfile(filename) and os.path.getsize(filename) > 0:#якщо файл існує та його розмір більший 0, видалити файл
    os.remove(filename)#видалити файл
with open(filename, 'a') as f:#створити і відкрити файл
    for i in output.split('\nn')[1:]:#розбити результат роботи функції на список по визначники, почати відлік з другого елементу
        f.write('Number - {}, Name - {}\n'.format(i.split('\t')[0][2:], translater(i.split('\t')[2])))
    f.close()
