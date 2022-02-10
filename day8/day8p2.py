def main():
	start_list = data_import()
	#print(start_list)
	#start_list = [start_list[0]]
	#start_list = [
	#	'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
	#]
	overall_sum = 0
	for i in start_list:
		# split into 2 strings
		start_index = i.find('|') + 2
		ans_str = i[start_index:len(i)]
		ans_list = ans_str.split(" ")
		quest_str = i[0:start_index - 3]
		quest_list = quest_str.split()
		full_list = ans_list + quest_list
		#print(quest_list)
		#print(ans_list)
		#print(full_list)
		#print(uniqe_str('abcd', 'bc'))
		bit_dict = {
			1: '',
			2: '',
			3: '',
			4: '',
			5: '',
			6: '',
			7: '',
		}

		ans_dict = {
			'0': '01110111',
			'1': '00010010',
			'2': '01011101',
			'3': '01011011',
			'4': '00111010',
			'5': '01101011',
			'6': '01101111',
			'7': '01010010',
			'8': '01111111',
			'9': '01111011'
		}

		#print(full_list)
		# general data
		two_l_list = list(set([x for x in full_list if len(x) == 2]))
		#print(two_l_list)

		three_l_list = list(set([x for x in full_list if len(x) == 3]))
		#print(three_l_list)

		four_l_list = list(set([x for x in full_list if len(x) == 4]))
		#print(four_l_list)

		five_l_list = list(set([x for x in full_list if len(x) == 5]))
		#print(five_l_list)

		six_l_list = list(set([x for x in full_list if len(x) == 6]))
		#print(six_l_list)

		seven_l_list = list(set([x for x in full_list if len(x) == 7]))
		#print(seven_l_list)

		# first deduction
		# subtract len3 from len2  bit1
		bit_1 = ''
		for i in three_l_list:
			for j in two_l_list:
				bit_1 = unique_str(i, j)
				if len(bit_1) == 1:
					bit_1 = bit_1[0]
					break

		bit_dict[1] = bit_1
		#print(f"A) {bit_dict}")

		# second deduction
		# len6 - len4 - sol = bit7
		bit_7_p1 = []
		bit_7 = []
		for i in six_l_list:
			for j in four_l_list:
				bit_7_p1.append(unique_str(i, j))
		#print(bit_7_p1)
		for i in bit_7_p1:
			for j in bit_dict.values():
				bit_7 = unique_str(i, j)
				#print(bit_7)
				if len(bit_7) == 1:
					bit_7 = bit_7[0]
					break
			if len(bit_7) == 1:
				break
		bit_dict[7] = bit_7
		#print(f"B) {bit_dict}")

		# third deduction
		# len4 + sol = 9 (len6)
		# len6(6) - 9 = bit5
		bit_5_p1 = []
		bit_5 = []
		check_str_nine = ''
		#print(four_l_list[0])
		temp_a = four_l_list[0]
		#print(bit_dict.values())
		temp_b = "".join(bit_dict.values())
		#check_str_nine = four_l_list[0] + ''.join(bit_dict.values())
		check_str_nine = temp_a + temp_b

		#print(check_str_nine)
		#print(six_l_list)
		for i in six_l_list:
			bit_5_p1 = unique_str(i, check_str_nine)
			#print(f'bit5_us: {bit_5_p1}')
			if len(bit_5_p1) == 1:
				bit_5 = bit_5_p1[0]
		#print(bit_5)
		bit_dict[5] = bit_5
		#print(f"C) {bit_dict}")

		#fouth deduction
		# leftover from all len6 + sol = 2
		# 2-len5 if sol_len2 then sub sol
		# bit 3
		# same loop len5-2 = len1 = bit6
		bit_3_p1 = []
		bit_3 = []
		bit_6_p1 = []
		bit_6 = []
		for i in six_l_list:
			for j in six_l_list:
				bit_6 = unique_str(i, j)
				if bit_6 and bit_6 not in bit_6_p1:
					bit_6_p1.append(bit_6[0])
		#print(bit_6_p1)
		bit_6_p1 = list(set(bit_6_p1))
		#print(bit_6_p1)
		check_str_six = ''.join(bit_6_p1) + ''.join(bit_dict.values())
		#print(check_str_six)
		for i in five_l_list:
			bit_6_p1 = unique_str(i, check_str_six)
			#print(bit_6_p1)
			if len(bit_6_p1) == 1 and not bit_6:
				bit_6 = bit_6_p1[0]

			bit_3_p1 = unique_str(check_str_six, i)
			#print(bit_3_p1)
			if len(bit_3_p1) == 3:
				bit_3 = [z for z in bit_3_p1 if z not in list(bit_dict.values())]

		bit_dict[6] = bit_6
		#print(f"D1) {bit_dict}")

		bit_3 = bit_3[0]
		bit_dict[3] = bit_3
		#print(f"D2) {bit_dict}")

		# grab str2 from before
		# str 2 - sol = bit4
		bit_4 = []
		bit_4 = unique_str(check_str_six, ''.join(bit_dict.values()))
		#print(bit_4)
		bit_4 = bit_4[0]
		bit_dict[4] = bit_4

		# str7 - sol = bit 2
		bit_2 = []
		for i in seven_l_list:
			bit_2 = unique_str(i, ''.join(bit_dict.values()))
			#print(bit_2)

		bit_2 = bit_2[0]
		bit_dict[2] = bit_2

		#print(f"Df) {bit_dict}")

		# decode ans list
		overall_str = ''
		for i in ans_list:
			overall_str += decode_str(i, bit_dict, ans_dict)
		overall_sum += int(overall_str)

	print(overall_sum)


def unique_str(a, b):
	#r_list = []
	# find chatacters in a, not in b
	r_list = [c for c in a if c not in b]

	return r_list


def decode_str(check_str, sol_dict, key_dict):
	r_str = ''
	key_str = '00000000'
	sol_dict_inv = dict(map(reversed, sol_dict.items()))
	key_list = list(key_str)
	#print(key_list)

	for c in check_str:
		key_list[sol_dict_inv[c]] = '1'
	#print(key_list)
	key_str = ''.join(key_list)
	#print(check_str)

	key_dict_inv = dict(map(reversed, key_dict.items()))
	r_str = key_dict_inv[key_str]
	return r_str


def data_import():
	day8_data_file = open('day8data.txt', 'r')
	day8_data_list = day8_data_file.read().splitlines()

	return day8_data_list


if __name__ == "__main__":
	main()

