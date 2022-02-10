import numpy as np
#from PIL import Image as im
import time
import itertools


def main():
	start_str, rules_dict = data_import()
	r = 40
	print(f'str: {r}')
	answer_dict = {}
	#print(f'start str: {start_str}')
	#print()
	#print(f'rules dict: {rules_dict}')
	#print()
	#init_list = []
	for n in range(len(start_str)-1):
		if start_str[n]+start_str[n+1] in answer_dict.keys():
			answer_dict[start_str[n]+start_str[n+1]] += 1
		else:
			answer_dict[start_str[n]+start_str[n+1]] = 1
		
	print(f'og ans: {answer_dict}')
	print()
	
	last_char = start_str[-1]
	for i in range(r):
		# create temp_dict
		temp_dict = {}
		# if count != 0 then update list
		for ans_dict_key, ans_dict_val in answer_dict.items():
			#print(f'')
			if ans_dict_val > 0:
				answer_dict[ans_dict_key] -= ans_dict_val
				insert_str = rules_dict[ans_dict_key]
				update_1 = ans_dict_key[0] + insert_str
				update_2 = insert_str + ans_dict_key[1]
				if update_1 in temp_dict.keys():
					temp_dict[update_1] += ans_dict_val
				else:
					temp_dict[update_1] = ans_dict_val
				
				if update_2 in temp_dict.keys():
					temp_dict[update_2] += ans_dict_val
				else:
					temp_dict[update_2] = ans_dict_val
		print(f'{i}, temp: {temp_dict}')
		print()
		# update main dict
		for temp_key, temp_val in temp_dict.items():
			if temp_key in answer_dict.keys():
				answer_dict[temp_key] += temp_val
			else:
				answer_dict[temp_key] = temp_val
	print(f'final answer: {answer_dict}')
	print()
	#count character from answer_dict
	char_count = {}
	for k, v in answer_dict.items():
		up1 = k[0]
		#up2 = k[1]
		if up1 in char_count.keys():
			char_count[up1] += v
		else:
			char_count[up1] = v
			
		#if up2 in char_count.keys():
		#	char_count[up2] += v
		#else:
		#	char_count[up2] = v
	# add last char
	if last_char in char_count.keys():
		char_count[last_char] += 1
	else:
		char_count[last_char] = 1
		
	print(f'chr_cnt: {char_count}')
	print()
	dict_values_list = char_count.values()
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
	
