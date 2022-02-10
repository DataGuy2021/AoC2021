import numpy as np

def main():
	main_list = data_import()
	#print(main_list)
	zeros_array = np.zeros([10,10], dtype=int)
	octo_array = np.zeros([10,10], dtype=int)
	#print(octo_array)
	for n, i in enumerate(main_list):
		octo_array[n] = list(map(int, [c for c in i]))
	print(octo_array)
	
	sync_list =[]
	flash_count = 0
	a = -1
	#for a in range(100):
	while len(sync_list) == 0:
		a+=1
		octo_array += 1
		flash_list = []
		
		# do > 9 logic
		flash_list = list(zip(*np.where(octo_array > 9)))
		#z = np.asarray(np.where(octo_array > 9)).T
		#print(flash_list)
		check_list = list(flash_list)
		#print(check_list)
		while len(check_list) > 0:
			# pop from check list
			(y, x) = check_list.pop(0)
			#add 1 around it
			cycle_list = []
			if x == 0 and y==0:
				# upper left x+1, y+1, x&y+1
				cycle_list.append((y+1,x))
				cycle_list.append((y+1,x+1))
				cycle_list.append((y,x+1))
			elif x==9 and y==9:
				# bot right, x-1, y-1, x&y-1
				cycle_list.append((y-1,x))
				cycle_list.append((y-1,x-1))
				cycle_list.append((y,x-1))
			elif x==0 and y==9:
				# bot left, x+1, y-1, (x+1,y-1)
				cycle_list.append((y-1,x))
				cycle_list.append((y-1,x+1))
				cycle_list.append((y,x+1))
			elif  x==9 and y==0:
				# top right x-1, y+1, (x-1,y+1)
				cycle_list.append((y+1,x))
				cycle_list.append((y+1,x-1))
				cycle_list.append((y,x-1))
			elif x==0 and 0<y<9:
				# left side x+, y+-
				cycle_list.append((y+1,x))
				cycle_list.append((y-1,x))
				cycle_list.append((y+1,x+1))
				cycle_list.append((y-1,x+1))
				cycle_list.append((y,x+1))
			elif x==9 and 0<y<9:
				# right side x-, y+-
				cycle_list.append((y+1,x))
				cycle_list.append((y-1,x))
				cycle_list.append((y+1,x-1))
				cycle_list.append((y-1,x-1))
				cycle_list.append((y,x-1))
			elif 0<x<9 and y==0:
				#top side x+-, y+
				cycle_list.append((y+1,x))
				cycle_list.append((y+1,x-1))
				cycle_list.append((y+1,x+1))
				cycle_list.append((y,x+1))
				cycle_list.append((y,x-1))
			elif 0<x<9 and y==9:
				#bottom x+-, y-
				cycle_list.append((y-1,x))
				cycle_list.append((y-1,x-1))
				cycle_list.append((y-1,x+1))
				cycle_list.append((y,x+1))
				cycle_list.append((y,x-1))
			else:
				# full check
				cycle_list.append((y-1,x-1))
				cycle_list.append((y-1,x+1))
				cycle_list.append((y+1,x-1))
				cycle_list.append((y+1,x+1))
				cycle_list.append((y,x+1))
				cycle_list.append((y,x-1))
				cycle_list.append((y+1,x))
				cycle_list.append((y-1,x))
				
			# go through cyle list, update array
			for j in cycle_list:
				if j not in flash_list:
					(a0, a1) = j
					octo_array[a0,a1] += 1
					if octo_array[a0,a1] > 9 and j not in flash_list:
						flash_list.append(j)
						check_list.append(j)
				
				#end cycle list
			
			
			# end check_list while loop
		
		
		# convert > 9 to zeros
		octo_array[octo_array>9] = 0
		if (octo_array == zeros_array).all():
			sync_list.append(a+1)
			print(sync_list)

		# count zeros add to total
		flash_count += (octo_array==0).sum()
	
		if a%1 == 0:
			print(a)
			#print(flash_count)
			print(octo_array)
			print(sync_list)
			print()
			
		#end for range loop
	print()	
	print(octo_array)
	#print(flash_count)
	print(sync_list)
			
	pass
	

def data_import():
    day11_data_file = open('day11data.txt', 'r')
    #day11_data_file = open('day11data_ut.txt', 'r')

    day11_data_list = day11_data_file.read().splitlines()

    return day11_data_list
	
	
if __name__ == "__main__":
    main()
    
