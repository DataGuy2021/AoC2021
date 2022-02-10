import numpy as np


def main():
	start_list = data_import()
	filtered_list = []
	part2_list = []
	for j in start_list:
		if j[0] == j[2] or j[1] == j[3]:
			filtered_list.append(j)
		else:
			part2_list.append(j)
			
	#print(filtered_list)
	sea_floor = np.zeros((1000, 1000), dtype=int)
	# [row, column] numpy indexing
	# [colum, row] AoC data
	for k in filtered_list:
		if k[0] == k[2]: # same column
			ndx = k[0]
			if k[1] > k[3]:
				low_r = k[3]
				high_r = k[1]
			else:
				low_r = k[1]
				high_r = k[3]
			
			print(low_r)
			print(high_r)
			for m in range(low_r, (high_r+1)):
				sea_floor[m,ndx] += 1
			
		else: # same row
			mdx = k[1]
			if k[0] > k[2]:
				low_r = k[2]
				high_r = k[0]
			else:
				low_r = k[0]
				high_r = k[2]
			for n in range(low_r, (high_r+1)):
				sea_floor[mdx,n] += 1
	
	# sea floor mapped
	# find intersections
	print(sea_floor)
	intersect_list = sea_floor[sea_floor > 1]
	print(intersect_list)
	print("part1: " + str(len(intersect_list)))
	
	# add part 2 list...
	for a in part2_list:
		x_pos = True
		x_low = a[0]
		x_high = a[2]
		if a[0] > a[2]:
			x_pos = False
			x_low = a[2]
			x_high = a[0]
		if x_pos:
			y_pos = True
			y_start = a[1]
			if a[1] > a[3]:
				y_pos = False
				#y_start = a[3]
		else:
			y_pos = True
			y_start = a[3]
			if a[3] > a[1]:
				y_pos = False
			
		n = 0
		for z in range(x_low, x_high+1):
			sea_floor[y_start+n, z ] += 1
			#if y_pos and x_pos:
			if y_pos:
				n += 1
			#elif x_pos and not y_pos:
				#n -= 1
			#elif not x_pos and y_pos:
				#n -= 1
			else:
				n -= 1
				
	print("part2:")
	print(sea_floor)
	intersect_list = sea_floor[sea_floor > 1]
	#print(intersect_list)
	print("part2: " + str(len(intersect_list)))

		
def data_import():
    day5_data_file = open('Day5data.txt', 'r')
    #day5_data_file = open('day5data_test.txt', 'r')
    
    day5_data_list = day5_data_file.read().splitlines()
    
    return_list = []
    for i in day5_data_list:
    	temp_data = i.replace('->', ',')
    	temp_list = temp_data.split(',')
    	temp_list = [int(x) for x in temp_list]
    	return_list.append(temp_list)
    #print(return_list)
    return return_list

	
if __name__ == "__main__":
    main()
    
