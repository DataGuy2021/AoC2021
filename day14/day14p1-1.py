import numpy as np
#from PIL import Image as im
import time


def main():
	start_str, rules_dict = data_import()
	r = 15
	print(f'list: {r}')
	#print(f'start str: {start_str}')
	#print()
	#print(f'rules dict: {rules_dict}')
	#print()
	start_list = list(start_str)
	for i in range(r):
		#sub_str = ''
		for j in range(len(start_list) - 1, -1, -1):
			if j == 0:
				break
			#print(f'start index: {j}')
			temp_str = start_list[j-1] + start_list[j]
			#print(f'temp_str: {temp_str}')
			insert_str = rules_dict[temp_str]
			start_list.insert(j, insert_str)
			#print(f'list update: {"".join([x for x in start_list])}')
			
			#print(f'sub_str: {sub_str}')
		#start_str = sub_str
		#print(f'index: {i}')
		#print(start_list)
		#print()
	# check for all uniqe characters
	uniqe_char_list = list(set(start_list))
	char_count_dict = {}
	for i in uniqe_char_list:
		char_count_dict[i] = start_list.count(i)
	
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
	
