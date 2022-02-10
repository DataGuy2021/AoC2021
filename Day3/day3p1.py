day3_data_file = open('day3data.txt','r')
day3_data_list = day3_data_file.read().splitlines()
# day3_data_list = list(map(str,day2_data_list))
gama_bin_str = day3_data_list.pop(0)
gama_bin_list = [int(x) for x in gama_bin_str]

for item in day3_data_list:
	for n in range(len(item)):
		int_item = int(item[n])
		int_gama = gama_bin_list[n]
		if int_item == 0:
			int_gama -= 1
		else:  # should be 1
			int_gama += 1
		gama_bin_list[n] = int_gama

eplison_bin_list = []
for x_index, x_value in enumerate(gama_bin_list):
	if x_value < 0:
		gama_bin_list[x_index] = 0
		eplison_bin_list.append(1)
	elif x_value > 0:
		gama_bin_list[x_index] = 1
		eplison_bin_list.append(0)
	else:
		eplison_bin_list.append(0)

gama_bin_str = ""a.join(map(str,gama_bin_list))
eplison_bin_str = "".join(map(str,eplison_bin_list))
gama_int = int(gama_bin_str, 2)
eplison_int = int(eplison_bin_str, 2)

print(eplison_int * gama_int)

		
