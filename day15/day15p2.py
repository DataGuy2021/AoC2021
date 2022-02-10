import numpy as np
import time
from collections import defaultdict


def dd_dv():
    return 9999


def main():
    t_m = time.perf_counter()
    main_list = data_import()
    # print(main_list)
    axis_0 = len(main_list)
    axis_1 = len(main_list[0])
    cave_array = np.zeros([axis_0, axis_1], dtype=int)
    
    for n, i in enumerate(main_list):
        cave_array[n] = list(map(int, [c for c in i]))
    #print(cave_array)
    
    cave_array = expand_cave(cave_array)
    #input('wait')
    axis_0 = axis_0 * 5
    axis_1 = axis_1 * 5
    
    #print(cave_array)
    #print()
    got_it_dict = defaultdict(dd_dv)
    start_index = (0, 0)
    start_val = cave_array[start_index]
    # print(f'{start_index}: {start_val}')
    path_list = [[0, (0, 1)], [0, (1, 0)]]
    final_path_list = []
    keep_checking = True
    a = 0 # while iteration
    r = 5000 # strip evey r passes
    r_s = 50000 # start strip after this count
    p = 0.5  # percent to strip
    e = 50 # dont remove if within this of min
    o_tt = 0
    keep_checking_c = 0
    while keep_checking:
        t_s = time.perf_counter()
        a += 1
        # print(f'pl: {path_list}')
        # print(f'fpl: {final_path_list}')
        #for x in range(len(path_list)):
        ck_indx = 0
        ck_lst = path_list.pop(ck_indx)
        # get last entry of list
        # print(path_list)
        og_0, og_1 = move_2, move_3 = move_0, move_1 = ck_lst[-1]
        # print(f'{og_0}, {og_1}')
        if move_0 != axis_0 - 1:
            move_0 += 1

        if move_1 != axis_1 - 1:
            move_1 += 1
        
        if move_2 != 0: # axis 0
            move_2 -= 1
        
        if move_3 != 0: # axis 1
            move_3 -= 1

        down_coor = (move_0, og_1)
        up_coor = (move_2, og_1)
        # print(f'down: {down_coor}')

        right_coor = (og_0, move_1)
        left_coor = (og_0, move_3)
        # print(f'right: {right_coor}')

        # check if same?
        out_list = []
        move_list = [down_coor, up_coor, right_coor, left_coor]
        move_list = list(set(move_list))
        
        for i in move_list:

            if i == (axis_0 - 1, axis_1 - 1):
                # it's the last piece
                # pop and append
                out_list = list(ck_lst)
                out_list.append(i)
                out_list = update_path(out_list, cave_array)
                final_path_list.append(out_list)
                keep_checking_c += 1
                #break
            elif i != ck_lst[-1]:
                #and right_coor not in got_it_list:
                #got_it_list.append(right_coor)
                temp_list = list(ck_lst)
                temp_list.append(i)
                temp_list = update_path(temp_list, cave_array)
                if got_it_dict[i] > temp_list[0]:
                    got_it_dict[i] = temp_list[0]
                    path_list.append(temp_list)
        
        #if a % r == 0 and a > r_s:
        if False:
        	# sort list, remove percentage
        	path_list = sorted(path_list, key = lambda x: -x[0])
        	strip_count = int(len(path_list) * p)
        	path_min = path_list[-1][0] + e
        	for x in range(strip_count):
        		check_strip = path_list.pop(0)
        		if check_strip[0] < path_min:
        			path_list.append(check_strip)
        path_list = sorted(path_list, key = lambda x: x[0])
        if a % 5000 == 0:
            t_e = time.perf_counter()
            #print(f'{a} ; runtime: {(t_e - t_s):0.3f} ; total: {(t_e - t_m):0.3f}')
            n_tt = t_e - t_m
            print(f'{a}; {path_list[0][1]}; pass {n_tt-o_tt:0.3f} ;total: {n_tt:0.3f}')
            o_tt = t_e - t_m
        if len(path_list) < 1 or keep_checking_c == 2:
            keep_checking = False

    min_path_count = 1000000  # ?!?
    for k in final_path_list:
        temp_count = get_sum_of_coor_2(k, cave_array)
        if temp_count < min_path_count:
            min_path_count = temp_count
            
    print(final_path_list)

    print(f'final answer: {min_path_count}')


def update_check(ck_list, main_list):
    rtn_bool = True
    for x in main_list:
        if x[1] == ck_list[1] and x[0] < ck_list[0]:
            
            rtn_bool = False
            break
    
    return rtn_bool


def expand_cave(start_arr):
    rtn_arr = start_arr
    arr_list = [start_arr]
    #print('A0')
    #print(start_arr)
    #print()
    
    for z in range(1,9):
        # create new array
        copy_arr = arr_list[-1]
        temp_arr = np.copy(copy_arr)
        temp_arr += 1
        temp_arr[temp_arr > 9] = 1
        #print(f'A{z}:')
        #print(temp_arr)
        #print()
        arr_list.append(temp_arr)
        
    #for f, g in enumerate(arr_list):
    #    print(f)
    #    print(g)
    #    print()
    
    # we have a list of arrays, now build
    # build first colums A0-A4 axis 1
    temp_arr_1 = arr_list[1]
    temp_arr_2 = arr_list[2]
    temp_arr_3 = arr_list[3]
    temp_arr_4 = arr_list[4]
    for r in range(1,5):
        rtn_arr = np.append(rtn_arr, arr_list[r], axis=1)
        temp_arr_1 = np.append(temp_arr_1, arr_list[r+1], axis = 1)
        temp_arr_2 = np.append(temp_arr_2, arr_list[r+2], axis = 1)
        temp_arr_3 = np.append(temp_arr_3, arr_list[r+3], axis = 1)
        temp_arr_4 = np.append(temp_arr_4, arr_list[r+4], axis = 1)
        
    rtn_arr =  np.append(rtn_arr, temp_arr_1, axis = 0)
    rtn_arr =  np.append(rtn_arr, temp_arr_2, axis = 0)
    rtn_arr =  np.append(rtn_arr, temp_arr_3, axis = 0)
    rtn_arr =  np.append(rtn_arr, temp_arr_4, axis = 0)
    
    #print(rtn_arr)
    
    return rtn_arr

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
    day15_data_file = open('day15data2.txt', 'r')
    #day15_data_file = open('day15data_ut.txt', 'r')
    #day15_data_file = open('day15data_ut1.txt', 'r')

    day15_data_list = day15_data_file.read().splitlines()

    return day15_data_list
	
	
if __name__ == "__main__":
    main()
    
