import numpy as np


def main():
	main_list = data_import()
	#print(main_list)
	axis_0 = len(main_list)
	axis_1 = len(main_list[0])
	cave_array = np.zeros([axis_0, axis_1], dtype=int)
	#print(octo_array)
	for n, i in enumerate(main_list):
		cave_array[n] = list(map(int, [c for c in i]))
	print(cave_array)
	
	
	start_index = (0, 0)
	start_val = cave_array[start_index]
	print(f'{start_index}: {start_val}')
	path_list = [[(0,1)],[(1,0)]]
	final_path_list = []
	keep_checking = True
	while keep_checking:
		print(f'pl: {path_list}')
		print(f'fpl: {final_path_list}')
		for x in range(len(path_list)-1):
			ck_indx = x
			ck_lst = path_list[x]
			# get last entry of list
			print(path_list)
			og_0, og_1 = move_0, move_1 = ck_lst[-1]
			print(f'{og_0}, {og_1}')
			if move_0 != axis_0 - 1:
				move_0 += 1
	
			if move_1 != axis_1 - 1:
				move_1 += 1
			
			down_coor = (move_0, og_1)
			print(f'down: {down_coor}')
		
			right_coor = (og_0, move_1)
			print(f'right: {right_coor}')
			
			# check if same?
			out_list = []
			
			if right_coor == (axis_0-1, axis_1-1):
				# it's the last piece
				# pop and append
				out_list = path_list.pop(ck_indx)
				out_list.append(right_coor)
				final_path_list.append(out_list)
			elif right_coor != ck_lst[-1]:
				path_list[ck_indx].append(right_coor)
			
			if right_coor != down_coor:
				# just do one update?
				if down_coor == (axis_0-1, axis_1-1):
					# it's the last piece
					# pop and append
					out_list = path_list.pop(ck_indx)
					out_list.append(down_coor)
					final_path_list.append(out_list)
				elif down_coor != ck_lst[-1]:
					temp_list = path_list[ck_indx]
					temp_list.append(down_coor)
					path_list.append(temp_list)
			
		if len(path_list) < 1:
			keep_checking = False
	
	min_path_count = 1000000. #?!?
	for k in final_path_list:
		temp_count = get_sum_of_coor(k, cave_array)
		if temp_count < min_path_count:
			min_path_count = temp_count
		
	print(f'final answer: {min_path_count}')


def get_sum_of_coor(coor_list, path_arr):
	rtn_sum = 0
	for j in coor_list:
		rtn_sum += path_arr[j]
	
	return rtn_sum

def check_location(check_0, check_1, max_0, max_1):
	axis_0 = 0
	axis_1 = 0

	return (axis_0, axis_1)


def data_import():
    #day15_data_file = open('day15data.txt', 'r')
    day15_data_file = open('day15data_ut.txt', 'r')

    day15_data_list = day15_data_file.read().splitlines()

    return day15_data_list
	
	
if __name__ == "__main__":
    main()
    
