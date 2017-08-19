from telnetconnector import connector

output = connector(str(input('Enter command to get field address:')))
if output[:2] == 'cc':
	print('You can\'t use \'change\' command, \'disp\' and \'list\' available')
else:
	f,d = {},{}
	lines = output.split('\n')
	for line in lines:
		if line.startswith('d'):
			d.update({
				len(d): line[1:]
			})
		elif line.startswith('f'):
			f.update({
				len(f): line[1:]
			})
		elif line.startswith('t'):
			break
		else:
			pass
	parse = {
		'fields': f,
		'data': d,
	}
	for key, value in parse.items():
		print('{0}: {1}'.format(key,value))
