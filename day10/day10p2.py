# import np as numpy

def main():
	check_list = data_import()
	#print(check_list)
	
	value_dict = {
		')':1,
		']':2,
		'}':3,
		'>':4
	}
	
	r_index_dict = {
		0:')',
		1:']',
		2:'}',
		3:'>'
	}
	
	
	
	#bad_list = []
	finish_list = []
	for i in check_list:
		#print(i)
		rb_list = [-1] # round
		sb_list = [-1] # square
		cb_list = [-1] # curly
		ab_list = [-1] # angle
		bad_item = False
		finish_str = ''
		
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
					bad_item = True
					break
		if not bad_item:
			# build proper end list
			# find max, add to finish
			# pop max
			keep_going = True
			while keep_going:
				print([rb_list, sb_list, cb_list, ab_list])
				m_max = list(map(max, [rb_list, sb_list, cb_list, ab_list]))
				#print(n_max)
				c_max = max(m_max)
				c_index = m_max.index(c_max)
				
				finish_str += r_index_dict[c_index]
				print(finish_str)
				if c_index == 0:
					rb_list.pop()
				elif c_index == 1:
					sb_list.pop()
				elif c_index == 2:
					cb_list.pop()
				elif c_index == 3:
					ab_list.pop()
				
				if len(rb_list) < 2 and len(sb_list) < 2 and len(cb_list) < 2 and len(ab_list) < 2:
					keep_going = False
			
			# do the final tally for this line
			total_score = 0
			for char in finish_str:
				total_score = (total_score * 5) + value_dict[char]
				
			print(total_score)
			finish_list.append(total_score)
	print(finish_list)
	# sort finish list, grab middle value
	finish_list.sort()
	
	middle_value = finish_list[len(finish_list)//2]
	print(middle_value) # do the middle of all values
	

def data_import():
    day10_data_file = open('day10data.txt', 'r')
    #day10_data_file = open('day10data_ut.txt', 'r')

    day10_data_list = day10_data_file.read().splitlines()

    return day10_data_list
	
	
if __name__ == "__main__":
    main()
    
