day1_data_file = open('day1data.txt','r')
day1_data_list = day1_data_file.readlines()
day1_data_list = list(map(int,day1_data_list))
final_count = 0

for n in range(len(day1_data_list)-1):
	if day1_data_list[n+1] > day1_data_list[n]:
		final_count += 1
		
print(final_count)

