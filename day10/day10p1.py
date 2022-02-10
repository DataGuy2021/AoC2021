# import np as numpy

def main():
	check_list = data_import()
	#print(check_list)
	
	value_dict = {
		')':3,
		']':57,
		'}':1197,
		'>':25137
	}
	
	bad_list = []
	for i in check_list:
		#print(i)
		rb_list = [-1] # round
		sb_list = [-1] # square
		cb_list = [-1] # curly
		ab_list = [-1] # angle
		
		for n, c in enumerate(i):
			if c == '(':
				rb_list.append(n)
			elif c == '[':
				sb_list.append(n)
			elif c == '{':
				cb_list.append(n)
			elif c == '<':
				ab_list.append(n)
			else: # its the closing
				# get max value so far
				#print([rb_list, sb_list, cb_list, ab_list])
				n_max = list(map(max, [rb_list, sb_list, cb_list, ab_list]))
				#print(n_max)
				b_max = max(n_max)
				b_index = n_max.index(b_max)
				if b_index == 0 and c == ')':
					# last one was a good bracket, pop it
					rb_list.pop()
				elif b_index == 1 and c == ']':
					sb_list.pop()
				elif b_index == 2 and c == '}':
					cb_list.pop()
				elif b_index == 3 and c == '>':
					ab_list.pop()
				else:
					# it's bad
					bad_list.append(value_dict[c])
					break
	print(bad_list)
	print(sum(bad_list))
		
		#rbl_count = i.count('(')
		#rbr_count = i.count(')')
		
		#sbl_count = i.count('[')
		#sbr_count = i.count(']')
		
		#cbl_count = i.count('{')
		#cbr_count = i.count('}')
		
		#abl_count = i.count('<')
		#abr_count = i.count('>')
		
		#print(f"rb:({rbl_count},{rbr_count})")
		#print(f"sb:({sbl_count},{sbr_count})")
		#print(f"cb:({cbl_count},{cbr_count})")
		#print(f"ab:({abl_count},{abr_count})")
		#print()
		
	pass
	

def data_import():
    day10_data_file = open('day10data.txt', 'r')
    #day10_data_file = open('day10data_ut.txt', 'r')

    day10_data_list = day10_data_file.read().splitlines()

    return day10_data_list
	
	
if __name__ == "__main__":
    main()
    
