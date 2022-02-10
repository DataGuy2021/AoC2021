# import np as numpy

def main():
	start_list = data_import()
	#print(start_list)
	count = [i for i in start_list if 1 < len(i) < 5 or len(i) == 7]
	print(len(count))
	

def data_import():
	day8_data_file = open('day8data.txt', 'r')
	day8_data_list = day8_data_file.read().splitlines()
	final_list = []
	for n, i in enumerate(day8_data_list):
		start_index = i.find('|') + 2
		update_str = i[start_index:len(i)]
		temp_list = update_str.split(" ")
		#day8_data_list[n] = update_str
		for j in temp_list:
			final_list.append(j)
	
	return final_list
	
	
if __name__ == "__main__":
    main()
    
