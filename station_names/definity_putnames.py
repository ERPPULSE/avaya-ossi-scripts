#!/usr/bin/python
# -*- coding: utf-8 -*-
# python v.3

from definity_connector import paramset
    
def retranslater(inputstring):
    '''функція перетворює текст укр мовою в англ'''
    inputstring = inputstring[:27].lstrip(' ')#station name fild length
    eng = 'qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./'
    ua = 'йцукенгшщзхї\фівапролджєячсмитьбю.'
    trans = str.maketrans(ua, eng)
    import unicodedata
    if inputstring != '' and unicodedata.name(inputstring[0]).partition(' ')[0] == 'CYRILLIC':
        return '~' + f'{inputstring.lower().translate(trans)}'
    else:
        return inputstring

with open('name2.txt', 'r') as f:
	content = f.readlines()
content = [x.strip().split(',') for x in content]
for i in content:
    paramset('ch sta ' + i[0], 'f8003ff00', retranslater(i[1]))
    #print(i[0], retranslater(i[1]))
