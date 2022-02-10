import numpy as np


def main():
    main_list = data_import()
    # print(main_list)
    axis_0 = len(main_list)
    axis_1 = len(main_list[0])
    cave_array = np.zeros([axis_0, axis_1], dtype=int)

    for n, i in enumerate(main_list):
        cave_array[n] = list(map(int, [c for c in i]))
    print(cave_array)

    start_index = (0, 0)
    start_val = cave_array[start_index]
    # print(f'{start_index}: {start_val}')
    path_list = [[0, (0, 1)], [0, (1, 0)]]
    final_path_list = []
    keep_checking = True
    a = 0 # while iteration
    r = 3 # strip evey r passes
    p = 0.5  # percent to strip
    e = 13 # dont remove if within this of min
    while keep_checking:
        a += 1
        # print(f'pl: {path_list}')
        # print(f'fpl: {final_path_list}')
        for x in range(len(path_list)):
            ck_indx = 0
            ck_lst = path_list.pop(ck_indx)
            # get last entry of list
            # print(path_list)
            og_0, og_1 = move_0, move_1 = ck_lst[-1]
            # print(f'{og_0}, {og_1}')
            if move_0 != axis_0 - 1:
                move_0 += 1

            if move_1 != axis_1 - 1:
                move_1 += 1

            down_coor = (move_0, og_1)
            # print(f'down: {down_coor}')

            right_coor = (og_0, move_1)
            # print(f'right: {right_coor}')

            # check if same?
            out_list = []

            if right_coor == (axis_0 - 1, axis_1 - 1):
                # it's the last piece
                # pop and append
                out_list = list(ck_lst)
                out_list.append(right_coor)
                out_list = update_path(out_list, cave_array)
                final_path_list.append(out_list)
            elif right_coor != ck_lst[-1]:
                temp_list = list(ck_lst)
                temp_list.append(right_coor)
                temp_list = update_path(temp_list, cave_array)
                if temp_list not in path_list:
                	path_list.append(temp_list)

            if right_coor != down_coor:
                # just do one update?
                if down_coor == (axis_0 - 1, axis_1 - 1):
                    # it's the last piece
                    # pop and append
                    out_list = list(ck_lst)
                    out_list.append(down_coor)
                    out_list = update_path(out_list, cave_array)
                    final_path_list.append(out_list)
                elif down_coor != ck_lst[-1]:
                    temp_list = list(ck_lst)
                    temp_list.append(down_coor)
                    temp_list = update_path(temp_list, cave_array)
                    if temp_list not in path_list:
                    	path_list.append(temp_list)
        # check 
        print(f'while iter: {a}')
        if a % r == 0:
        	# sort list, remove percentage
        	path_list = sorted(path_list, key = lambda x: -x[0])
        	strip_count = int(len(path_list) * p)
        	path_min = path_list[-1][0] + e
        	for x in range(strip_count):
        		check_strip = path_list.pop(0)
        		if check_strip[0] < path_min:
        			path_list.append(check_strip)


        if len(path_list) < 1:
            keep_checking = False

    min_path_count = 1000000  # ?!?
    for k in final_path_list:
        temp_count = get_sum_of_coor_2(k, cave_array)
        if temp_count < min_path_count:
            min_path_count = temp_count

    print(f'final answer: {min_path_count}')


def get_sum_of_coor(coor_list, path_arr):
    rtn_sum = 0
    for j in coor_list:
        rtn_sum += path_arr[j]

    return rtn_sum
    
    
def get_sum_of_coor_2(coor_list, path_arr):
    rtn_sum = coor_list[0]
    
    rtn_sum += path_arr[coor_list[1]]

    return rtn_sum
    
    
def update_path(input_list, input_arr):
	rtn_list = []
	# should be 3 items in list
	# 0 is sum / 1 is old location / 2 is new
	# add old locatio to sum, rtn 2 item list
	new_sum = input_list[0] + input_arr[input_list[1]]
	rtn_list.append(new_sum)
	rtn_list.append(input_list[2])
	
	return rtn_list
	

def data_import():
    day15_data_file = open('day15data.txt', 'r')
    #day15_data_file = open('day15data_ut.txt', 'r')
    #day15_data_file = open('day15data_ut1.txt', 'r')

    day15_data_list = day15_data_file.read().splitlines()

    return day15_data_list
	
	
if __name__ == "__main__":
    main()
    
