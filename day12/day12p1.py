# import numpy as np

def main():
	map_dict = data_import()
	print(map_dict)
	print()
	# build first list(s) from start
	master_list = []
	start_list = map_dict['start']
	for sl_i in start_list:
		master_list.append([sl_i])
	#print(master_list)
	
	# initalize loop variables
	keep_going = True
	z = 0
	
	# loop creating paths
	while keep_going or z < 1000:
		z += 1
		#print()
		#print(master_list)
		# pop the first item
		current_list = master_list.pop(0)
		#print(f"current: {current_list}")
		# grab last item in first list
		current_cave = current_list[-1]
		# grab new destinations
		if current_cave == 'end':
			master_list.append(current_list)
		else:
			parse_list = map_dict[current_cave]
			#print(f"parse: {parse_list}")
			# go over parse list
			for j in parse_list:
				temp_list = list(current_list)
				temp_list.append(j)
				#print(f"temp: {temp_list}")
				if good_path(temp_list):
					master_list.append(temp_list)
			if check_done(master_list):
				keep_going = False
	
	# remove dups
	master_list2 = []
	update_bool = False
	for i in master_list:
		list_equal = 0
		for j in master_list:
			if i == j:
				list_equal += 1
		
		if list_equal < 2:
			master_list2.append(i)
	
	for a in master_list2:		
		print(a)
	print(len(master_list2))
	
	
def check_done(end_list):
	rtn_bool_1 = False
	for k in end_list:
		if k[-1] == 'end':
			rtn_bool_1 = True
		else:
			rtn_bool_1 = False
			break

	return rtn_bool_1
	
	
def good_path(sub_list):
	rtn_bool = False
	# check for the same lowercase letter
	check_set = set([x for x in sub_list if sub_list.count(x) > 1])
	#print(f"sub(good path): {check_set}")
	if check_set:
		for f in check_set:
			if not f.islower():
				rtn_bool = True
			else:
				rtn_bool = False
				break
	else:
		rtn_bool = True
	
	return rtn_bool
	

def data_import():
    #day12_data_file = open('day12data.txt', 'r')
    day12_data_file = open('day12data_ut.txt', 'r')
    #day12_data_file = open('day12data_ut1.txt', 'r')
    #day12_data_file = open('day12data_ut2.txt', 'r')

    day12_data_list = day12_data_file.read().splitlines()
    
    #build dict
    return_dict = {
    	'start': []
    }
    
    # split connectiona
    for a in day12_data_list:
    	[c1, c2] = a.split('-')
    	
    	if c1 in return_dict.keys() and c2 != 'start':
    		temp_list = return_dict[c1]
    		temp_list.append(c2)
    		return_dict[c1] = temp_list
    		
    	if c2 in return_dict.keys() and c1 != 'start':
    		temp_list = return_dict[c2]
    		temp_list.append(c1)
    		return_dict[c2] = temp_list
    		
    	if c1 not in return_dict.keys() and c1 != 'end' and c2 != 'start':
    		return_dict[c1] = [c2]
    	if c2 not in return_dict.keys() and c2 != 'end' and c1 != 'start':
    		return_dict[c2] = [c1]
    	

    return return_dict
  
	
if __name__ == "__main__":
    main()
    
