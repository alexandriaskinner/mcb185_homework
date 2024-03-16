#82transfac.py by Alexandria Skinner

import sys
import gzip
import json

pwms = []
i = 0
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		word = line.split()
		
		if word[0] == 'ID':
			pwms.append({'id': word[1], 'pwm': []})
		
		if word[0][0] == '0': 
			pwms[i]['pwm'].append({
				'A': word[1],
				'C': word[2],
				'G': word[3],
				'T': word[4]})
		
		if word[0] == '//': i += 1

print(json.dumps(pwms, indent=4))			