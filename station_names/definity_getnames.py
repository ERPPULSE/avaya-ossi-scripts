#!/usr/bin/python
# -*- coding: utf-8 -*-
# python v.3

import os
from definity_connector import connector

def translater(inputstring):
    '''функція перетворює текст введений анг. літерами на
українскі літери та робить всі перші букви слів великими'''
    eng = 'qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./'
    ua = 'йцукенгшщзхї\фівапролджєячсмитьбю.'
    trans = str.maketrans(eng, ua)
    if len(inputstring) > 0 and inputstring[0] == '~':
        return f'{inputstring.lower().translate(trans).title()}'[1:]
    else:
        return inputstring
    
output = connector('list sta 2000 count 800')
filename = 'name.txt'
if os.path.isfile(filename) and os.path.getsize(filename) > 0:
    os.remove(filename)
with open(filename, 'a') as f:
    for i in output.split('\nn')[1:]:
        f.write('{}, {}\n'.format(i.split('\t')[0][2:], translater(i.split('\t')[2])))
    f.close()
