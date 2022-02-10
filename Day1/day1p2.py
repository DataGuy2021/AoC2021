day1_data_file = open('day1data.txt','r')
day1_data_list = day1_data_file.readlines()
day1_data_list = list(map(int,day1_data_list))
final_count = 0

for n in range(len(day1_data_list)-3):
	if sum(day1_data_list[n+1:n+4]) > sum(day1_data_list[n:n+3]):
		final_count += 1
		
print(final_count)
