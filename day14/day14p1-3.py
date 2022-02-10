import numpy as np
#from PIL import Image as im
import time


def main():
	start_str, rules_dict = data_import()
	r = 18
	print(f'dict: {r}')
	#print(f'start str: {start_str}')
	#print()
	#print(f'rules dict: {rules_dict}')
	#print()
	start_dict = {}
	for v, c in enumerate(start_str):
		if c in start_dict.keys():
			temp_list = start_dict[c]
			temp_list.append(v)
			start_dict[c] = temp_list
		else:
			start_dict[c] = [v]
		
	
	for i in range(r):
		print(f'run: {r}')
		start_i = time.process_time()
		sub_dict = ''
		# find max 
		range_max = max(start_dict.values(), key=max)
		for j in range(range_max - 1):
			#print(f'start str_index: {j}')
			temp_str = start_str[j] + start_str[j+1]
			#print(f'temp_str: {temp_str}')
			insert_str = rules_dict[temp_str]
			if j == 0:
				temp_str = temp_str[0] + insert_str + temp_str[1]
			else:
				temp_str = insert_str + temp_str[1]
			#print(f'temp_str update: {temp_str}')
			sub_str += temp_str
			#print(f'sub_str: {sub_str}')
		start_dict = sub_dict
		end_i = time.process_time()
		print(f'time: {end_i - start_i}')
		print()
		
	# check for all uniqe characters
	uniqe_char_list = list(set(start_str))
	char_count_dict = {}
	for i in uniqe_char_list:
		char_count_dict[i] = start_str.count(i)
	
	dict_values_list = char_count_dict.values()
	max_char_count = max(dict_values_list)
	min_char_count = min(dict_values_list)
	print(max_char_count-min_char_count)
	
	
def data_import():
    day14_data_file = open('day14data.txt', 'r')
    #day14_data_file = open('day14data_ut.txt', 'r')
    
    day14_data_list = day14_data_file.read().splitlines()
    keep_going = True
    poly_str = ''
    
    while keep_going:
    	line_item = day14_data_list.pop(0)
    	if line_item:
    		poly_str = line_item
    	else:
    		keep_going = False
	    	break
	    
	# add next to fold list
	#keep_going = True
    rule_dict = {}
    for i in day14_data_list:
    	k, v = i.split(' -> ')
    	rule_dict[k] = v
    	

    # print(bingo_cards_list)
    return poly_str, rule_dict
    
	
	
if __name__ == "__main__":
	start = time.process_time()
	main()
	end = time.process_time()
	print(end-start)
	
