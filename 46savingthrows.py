#46savingthrows.py by Alexandria Skinner

import random

def prob_save(dis_adv, DC):
	#dis_adv can be 'none', 'adv', or 'dis'
	total = 0
	success = 0
	for i in range(10000):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)

		if dis_adv == 'none': roll = d1
		if dis_adv == 'dis':
			if d1 > d2: roll = d2
			else:       roll = d1
		if dis_adv == 'adv':
			if d1 > d2: roll = d1
			else:       roll = d2
		if roll >= DC: success += 1
		total += 1
	return(success / total)

print(f'Difficulty Class:\t5\t10\t15')

print('no advantage:\t', prob_save('none', 5), prob_save('none', 10), prob_save('none', 15), sep='\t')
print('with advantage:\t', prob_save('adv', 5), prob_save('adv', 10), prob_save('adv', 15), sep='\t')
print('with disadvantage:', prob_save('dis', 5), prob_save('dis', 10), prob_save('dis', 15), sep='\t')
