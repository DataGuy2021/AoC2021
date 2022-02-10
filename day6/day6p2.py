def main():
	#input_list = [3,4,3,1,2]  # test list
	input_list = [1,1,1,1,2,1,1,4,1,4,3,1,1,1,1,1,1,1,1,4,1,3,1,1,1,5,1,3,1,4,1,2,1,1,5,1,1,1,1,1,1,1,1,1,1,3,4,1,5,1,1,1,1,1,1,1,1,1,3,1,4,1,1,1,1,3,5,1,1,2,1,1,1,1,4,4,1,1,1,4,1,1,4,2,4,4,5,1,1,1,1,2,3,1,1,4,1,5,1,1,1,3,1,1,1,1,5,5,1,2,2,2,2,1,1,2,1,1,1,1,1,3,1,1,1,2,3,1,5,1,1,1,2,2,1,1,1,1,1,3,2,1,1,1,4,3,1,1,4,1,5,4,1,4,1,1,1,1,1,1,1,1,1,1,2,2,4,5,1,1,1,1,5,4,1,3,1,1,1,1,4,3,3,3,1,2,3,1,1,1,1,1,1,1,1,2,1,1,1,5,1,3,1,4,3,1,3,1,5,1,1,1,1,3,1,5,1,2,4,1,1,4,1,4,4,2,1,2,1,3,3,1,4,4,1,1,3,4,1,1,1,2,5,2,5,1,1,1,4,1,1,1,1,1,1,3,1,5,1,2,1,1,1,1,1,4,4,1,1,1,5,1,1,5,1,2,1,5,1,1,1,1,1,1,1,1,1,1,1,1,3,2,4,1,1,2,1,1,3,2]  # real list
	final_length = 0
	refine_dict = {
		0:0,
		1:0,
		2:0,
		3:0,
		4:0,
		5:0,
		6:0,
		7:0,
		8:0
	}
	refine_list = input_list
	#refine_list = input_list
	# put initial data in dict
	for i in refine_list:
		refine_dict[i] += 1
		
	for a in range(1,257):
		new_8 = refine_dict[0]
		new_7 = refine_dict[8]
		new_6 = refine_dict[7]+refine_dict[0]
		new_5 = refine_dict[6]
		new_4 = refine_dict[5]
		new_3 = refine_dict[4]
		new_2 = refine_dict[3]
		new_1 = refine_dict[2]
		new_0 = refine_dict[1]
		refine_dict = {
			0:new_0,
			1:new_1,
			2:new_2,
			3:new_3,
			4:new_4,
			5:new_5,
			6:new_6,
			7:new_7,
			8:new_8
		}
		
	for k, v in refine_dict.items():
		final_length += v
			
	print(final_length)
	
	
if __name__ == "__main__":
    main()
    
