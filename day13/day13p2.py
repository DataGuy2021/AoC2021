import numpy as np
from PIL import Image as im


def main():
	dot_list, fold_list, a0_m, a1_m = data_import()
	
	answer_list = []
	#print(dot_list)
	#print()
	#print(fold_list)
	
	paper_arr = np.zeros((a0_m+1, a1_m+1), dtype = int)
	
	for i in dot_list:
		(a1, a0) = i
		paper_arr[a0, a1] = 1
	#print(paper_arr)
	#print()
	
	check_1 = False
	for j in fold_list:
		#print(j)
		
		# fold y
		axis_fold_index_y = j['y']
		reg_arr_y = paper_arr[:axis_fold_index_y, :]
		fold_arr_y = paper_arr[axis_fold_index_y+1:, :]
		
		#print('reg_arr_y')
		#print(reg_arr_y)
		#print()
		
		fold_arr_y = np.flipud(fold_arr_y)
		#print('fold_arr_y')
		#print(fold_arr_y)
		#print()
		
		# check lengths and pad if needed
		
		paper_arr_fold = pad_array(reg_arr_y,  fold_arr_y, 0)
		#print('paper_arr_fold after y')
		#print(paper_arr_fold)
		#print()
		
		#fold x
		axis_fold_index_x = j['x']
		reg_arr_x = paper_arr_fold[:, :axis_fold_index_x]
		fold_arr_x = paper_arr_fold[:, axis_fold_index_x+1:]
		
		#print('reg_arr_x')
		#print(reg_arr_x)
		#print()
		fold_arr_x = np.fliplr(fold_arr_x)
		#print('fold_arr_x')
		#print(fold_arr_x)
		#print()
		
		paper_arr_final = pad_array(fold_arr_x, reg_arr_x, 1)
		#print('paper_arr_fold after x')
		#print(paper_arr_fold)
		#print()
		
		# normalize array
		paper_arr_done = np.where(paper_arr_final > 0, 1, paper_arr_final)
		
		# get count 
		#dot_count = np.count_nonzero(paper_arr_fold)
		#print(f"{j}: count: {dot_count}")
		#print()
		
		if check_1:
			break
		answer_list.append(paper_arr_done)
	
	output_list = trim_array(answer_list)
	file_output(output_list)
	image_output(output_list)
	print('done')
	
def image_output(arr_list):
	for i, v in enumerate(arr_list):
		new_arr = np.where(v==1,255,v)
		#print(new_arr.dtype)
		new_arr_dt = new_arr.astype('uint8')
		image_data = im.fromarray(new_arr_dt)
		save_str = f'{i}.png'
		image_data.save(save_str)
	pass
	
def trim_array(a):
	out_list = []
	z = 0
	for x in a:
		z+=1
		a_zero, a_one = x.nonzero()
		#print(str(z))
		#print(a_zero)
		#print(a_one)

		s0 = np.min(a_zero) 
		s1 = np.min(a_one)
		
		e0 = np.max(a_zero)+1
		e1 = np.max(a_one)+1
		#print(f'{s0}:{e0},{s1}:{e1}')
		
		temp_arr = x[s0:e0, s1:e1]
		#temp_arr[temp_arr > 1] == 1
		#print(temp_arr)
		out_list.append(temp_arr)
	return out_list
	
	
def file_output(output_list):
	output_file = open('day13output.txt', 'w')
	for a, z in enumerate(output_list):
		output_file.write(str(a))
		output_file.write('\n')
		for x in z:
			output_file.write(str(x))
			output_file.write('\n')
		output_file.write('\n')
		output_file.write('\n')

	output_file.close()
	pass
	
	
def pad_array(start_arr, fold_arr, axis_name):
	#temp_arr = np.ndarray()
	start_arr_len = start_arr.shape[axis_name]
	#print(f'start_len: {start_arr_len}')
	fold_arr_len = fold_arr.shape[axis_name]
	#print(f'fold_len: {fold_arr_len}')
	add_on = abs(start_arr_len - fold_arr_len)
	#print(f'add_on: {add_on}')
	if axis_name == 0:
		other_axis = 1
		axis_0_add = add_on
		axis_1_add = fold_arr.shape[other_axis]
	else:
		other_axis = 0
		axis_1_add = add_on
		axis_0_add = fold_arr.shape[other_axis]
	# flipping up check axis zero length
	# short one gets zeros added to top of array
	add_arr = np.zeros((axis_0_add, axis_1_add), dtype = int)
	
	if start_arr_len > fold_arr_len:
		# add to fold_arr
		# add to end
		fold_arr = np.concatenate((fold_arr, add_arr), axis = axis_name)	
	elif fold_arr_len > start_arr_len:
		# add to start_arr
		start_arr = np.concatenate((add_arr, start_arr), axis = axis_name)
	# add arrays
	temp_arr = start_arr + fold_arr
	
	return temp_arr
	

def data_import():
    day13_data_file = open('day13data.txt', 'r')
    #day13_data_file = open('day13data_ut.txt', 'r')
    #day13_data_file = open('day13data_ut1.txt', 'r')
    
    day13_data_list = day13_data_file.read().splitlines()
    keep_going = True
    dots_list =[]
    a0_max = 0
    a1_max = 0
    while keep_going:
    	line_item = day13_data_list.pop(0)
    	if line_item:
    		udl = (a1t, a0t) = tuple([int(i) for i in line_item.split(',')])
    		if a1t > a1_max:
    			a1_max = a1t
    		if a0t > a0_max:
    			a0_max = a0t
    		dots_list.append(udl)
    	else:
    		keep_going = False
	    	break
	    
	# add next to fold list
	#keep_going = True
    folds_list =[]
    for i in day13_data_list:
    	start_index = i.find('=')
    	folds_list.append(tuple(i[start_index-1:len(i)+1].split('=')))
    
    folds_dict_list = []
    temp_dict = {}
    for j in folds_list:
    	if len(temp_dict) == 2:
    		temp_dict = {}
    	temp_dict[j[0]] = int(j[1])
    	if len(temp_dict) == 2:
    		folds_dict_list.append(temp_dict)
    	

    # print(bingo_cards_list)
    return dots_list, folds_dict_list, a0_max, a1_max
    
	
	
if __name__ == "__main__":
    main()
    
