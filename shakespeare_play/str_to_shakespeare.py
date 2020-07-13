import itertools, math

def get_adj(n):
	gen = itertools.cycle(['red', 'green', 'blue'])
	ans = []
	for _ in range(n):
		ans.append(next(gen))
	return ' '.join(ans)

def output_char(x):
	cmd = 'Hamlet: You are nothing! '
	num = ord(x)
	first = True
	while num > 0:
		max_two = int(math.log(num, 2))
		num -= pow(2, max_two)
		if first:
			cmd += 'You are a ' + get_adj(max_two) + ' tree! '
			first = False
		else:
			cmd += 'You are as lovely as the sum of a ' + get_adj(max_two) + ' tree and thyself! '
	cmd += 'Speak your mind!'
	return cmd
		
def output_string(string):
	return '\n'.join([output_char(x) for x in string])

header = '''A long lost play about trees, written exclusively by Shakespeare for RGBSec.

Romeo, apparently a rapidly changing multicolored tree.
Hamlet, a person who can't make up his mind.


                    Act I: Colorful Tree.

                    Scene I: Fast-changing Tree.

[Enter Hamlet and Romeo]

'''

footer = '\n[Exeunt]\n'



with open('play', 'w') as f:
	f.write(header + output_string('VmxSQ2EyTXlVbGhWYTFacFRXMVNVMWxzVW5OTmJHeFpZa1ZPYUdKVldscFZWekExV1Zaa1JtRjZhejA9') + footer)

