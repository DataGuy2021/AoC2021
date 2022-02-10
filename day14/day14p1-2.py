import numpy as np
#from PIL import Image as im
import time


def main():
	start_str, rules_dict = data_import()
	r = 15
	print(f'numpy: {r}')
	#print(f'start str: {start_str}')
	#print()
	#print(f'rules dict: {rules_dict}')
	#print()
	str_arr = np.empty(0, dtype = ('U', 10))
	for c in start_str:
		str_arr = np.append(str_arr, c)
	#print(f'str_arr: {str_arr}')
	#print()
	for i in range(r):
		#sub_str = ''
		for j in range(len(str_arr) - 1, -1, -1):
			if j == 0:
				break
			#print(f'start index: {j}')
			temp_str = str_arr[j-1] + str_arr[j]
			#print(f'temp_str: {temp_str}')
			insert_str = rules_dict[temp_str]
			str_arr = np.insert(str_arr, j, insert_str)
			#print(f'list update: {"".join([x for x in start_list])}')
			
			#print(f'sub_str: {sub_str}')
		#start_str = sub_str
		#print(f'index: {i}')
		#print(''.join(list(str_arr)))
		#print()
	# check for all uniqe characters
	uniqe_char_list = list(np.unique(str_arr))
	char_count_dict = {}
	for i in uniqe_char_list:
		char_count_dict[i] = np.count_nonzero(str_arr == i)
	
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
	
