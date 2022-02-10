import numpy as np


def main():
    b_calls, b_card_list = data_import()
    # print(type(b_calls)) list of call numbers
    # print(b_calls) 
    # print(b_card_list) list of numpy arrays
    final_call = 0
    array_sum = 0
    p_n = 0
    for i in b_calls:
    	#while True:
    	for a_i in range(len(b_card_list)):
    		temp_array = b_card_list.pop(0)
    		
    		temp_array[temp_array==i] = -1
    		
    		if (np.array(temp_array==-1).all(axis=0).any()) or (np.array(temp_array==-1).all(axis=1).any()):
    			# don't append back'
    			if len(b_card_list) == 0:	
    				print(temp_array)
    				temp_array[temp_array==-1] = 0
    				final_call = i
    				array_sum = np.sum(temp_array)
    				break
    		else:
    			b_card_list.append(temp_array)
    			
    	p_n = i
    	if final_call and array_sum:
    		break
    		
    print(final_call)
    print(array_sum)
    print(final_call * array_sum)
	

def data_import():
    day4_data_file = open('day4data.txt', 'r')
    day4_data_list = day4_data_file.read().splitlines()
    bingo_calls = day4_data_list.pop(0).split(',')
    day4_data_list.pop(0)    # remove first blank line
    bingo_calls = [int(x) for x in bingo_calls]
    # print(bingo_calls)
    # np_bingo_cards = np.ndarray
    bingo_cards_list = []  # add numpy arrays as elements
    np_temp_arr = np.ndarray(shape=(5, 5), dtype=int)
    # print(np_temp_arr)
    ndx = 0
    for i in day4_data_list:
        if not i:  # i is empty line, store data, start over
            bingo_cards_list.append(np_temp_arr)
            np_temp_arr = np.ndarray(shape=(5, 5), dtype=int)
            ndx = 0

        else:  # it's not empty, add to current array
            np_temp_arr[ndx] = list(map(int, i.split()))
            ndx += 1
    # add last card
    bingo_cards_list.append(np_temp_arr)

    # print(bingo_cards_list)
    return bingo_calls, bingo_cards_list


if __name__ == "__main__":
    main()
