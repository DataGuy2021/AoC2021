import numpy as np
from PIL import Image as im

def main():
	dot_list, fold_list, a0_m, a1_m = data_import()
	
	print(dot_list)
	print()
	print(fold_list)
	
	paper_arr = np.zeros((a0_m+1, a1_m+1), dtype = int)
	
	for i in dot_list:
		(a1, a0) = i
		paper_arr[a0, a1] = 1
	print(paper_arr)
	print()
	
	check_1 = False
	for j in fold_list:
		print(j)
		axis_fold_index = int(j[1])
		if j[0] == 'y':
			reg_arr = paper_arr[:axis_fold_index, :]
			fold_arr = paper_arr[axis_fold_index+1:, :]
			
			print(reg_arr)
			print()
			
			fold_arr = np.flipud(fold_arr)
			print(fold_arr)
		
		if j[0] == 'x':
			reg_arr = paper_arr[:, :axis_fold_index]
			fold_arr = paper_arr[:, axis_fold_index+1:]
			
			print(reg_arr)
			print()
			fold_arr = np.fliplr(fold_arr)
			print(fold_arr)
		
		paper_arr = fold_arr + reg_arr
		print()
		print(paper_arr)
		
		# normalize array
		paper_arr[paper_arr > 1] == 1
		
		# get count 
		dot_count = np.count_nonzero(paper_arr)
		print()
		print(f"{j}: count: {dot_count}")
		print()
		
		if check_1:
			break
	print(paper_arr)
	pass
	

def data_import():
    #day13_data_file = open('day13data.txt', 'r')
    day13_data_file = open('day13data_ut.txt', 'r')
    
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
    	

    # print(bingo_cards_list)
    return dots_list, folds_list, a0_max, a1_max
    
	
	
if __name__ == "__main__":
    main()
    
