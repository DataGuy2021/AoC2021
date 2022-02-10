day3_data_file = open('day3data.txt','r')
day3_data_list = day3_data_file.read().splitlines()

most_comm_list = []
less_comm_list = []
print(len(day3_data_list[0]))
for n in range(len(day3_data_list[0])):
	
	zeros_list = []
	ones_list = []
	zero_count = 0
	one_count = 0
	print(n)
	print(f"mc:{len(most_comm_list)}")
	print(f"lc:{len(less_comm_list)}")
	if most_comm_list and less_comm_list:
		# tun through lists
		#print("we made it!!!")
		if len(most_comm_list) > 1:
			for item_mc in most_comm_list:
				if int(item_mc[n]) == 0:
					zero_count += 1
					zeros_list.append(item_mc)
				else:
					one_count += 1
					ones_list.append(item_mc)
			
			if zero_count > one_count:
				most_comm_list = zeros_list
			else:
				most_comm_list = ones_list
		
		if len(less_comm_list) > 1:
			zeros_list = []
			ones_list = []
			for item_lc in less_comm_list:
				if int(item_lc[n]) == 0:
					zero_count += 1
					zeros_list.append(item_lc)
				else:
					one_count += 1
					ones_list.append(item_lc)
			
			if one_count < zero_count:
				less_comm_list = ones_list
			else:
				less_comm_list = zeros_list
			
		
	else:
		# starting data
		for item in day3_data_list:
			if int(item[n]) == 0:
				zero_count += 1
				zeros_list.append(item)
			else:
				one_count += 1
				ones_list.append(item)
				
		if zero_count > one_count:
			most_comm_list = zeros_list
			less_comm_list = ones_list
		elif one_count > zero_count:
			most_comm_list = ones_list
			less_comm_list = zeros_list
		else: # same on first?
			most_comm_list = ones_list
			less_comm_list = zeros_list
			
		print(f"MC-OG: {len(most_comm_list)}")
		print(f"LC-OG: {len(less_comm_list)}")
		
	
	if len(most_comm_list) == 1 and len(less_comm_list) == 1:
		break
		
print(f"F_MC: {len(most_comm_list)}")
print(f"F_LC: {len(less_comm_list)}")

oxygen_rate_str = "".join(map(str,most_comm_list))
oxygen_rate_int = int(oxygen_rate_str, 2)

cotwo_rate_str = "".join(map(str,less_comm_list))
cotwo_rate_int = int(cotwo_rate_str, 2)
		


print(cotwo_rate_int * oxygen_rate_int)
