# import numpy as np


def main():
    print('main start')
    main_str_list = data_import()
    start_str = main_str_list[0]
    print(start_str)

    bin_str = hex_to_bin(start_str)
    print(bin_str)

    # list of lists with data
    keep_going = True
    while keep_going:
        decode_list = decode_bin(bin_str)

    pass
    

def decode_bin_11(c_str, c_count):
    rtn_list = []
    rtn_str = ''
    
    
    return rtn_list, rtn_str


def decode_bin(b_str):
    rtn_list = []
    keep_going = True
    vr_list = []

    while keep_going:
        vr, b_str = b_str[0:3], b_str[3:len(b_str)]
        print(vr)
        print(b_str)
        vr_int = int(vr, 2)
        print(vr_int)
        vr_list.append(vr_int)

        tp, b_str = b_str[0:3], b_str[3:len(b_str)]
        print(tp)
        print(b_str)
        tp_int = int(tp, 2)
        print(tp_int)

        # check version 
        if tp_int == 4:
            # literal value, get all packet
            b_str, lit_int = packet_literal(b_str)
            print(b_str)
            print(lit_int)
            pass
        else:  # operator value
            lgth, b_str = b_str[0:1], b_str[1:len(b_str)]
            print(lgth)
            print(b_str)
            if lgth == 0:
                # get 15 chars for sub pack
                op_0_list = []
                sub_len, b_str = b_str[0:15], b_str[15:len(b_str)]
                sub_len_int = int(sub_len, 2)
                new_set, b_str = b_str[0:sub_len_int], b_str[sub_len_int:len(b_str)]
                op_0_list = decode_bin(new_set)

                pass
            else:  # lgth == 1
                # get 11 char for 
                op_1_list = []
                sub_len, b_str = b_str[0:11], b_str[11:len(b_str)]
                sub_len_int = int(sub_len, 2)
                # check sub_len_int amount of packets?!?
                op_0_list, b_str = decode_bin_11(b_str, sub_len_int)
                
                pass

            pass
        if len(b_str) == 0:
            keep_going = False
    op_0_list += op_1_list
    vr_list += op_0_list

    return rtn_list


def packet_literal(check_str):
    rtn_str = ''
    rtn_int = 0
    keep_itup = True
    lit_list = []

    while keep_itup:
        check_bit, check_str = check_str[0:1], check_str[1:len(check_str)]
        print(check_bit)
        print(check_str)
        print()

        lit_val, check_str = check_str[0:4], check_str[4:len(check_str)]
        lit_list.append(lit_val)

        if check_bit == '0':
            keep_itup = False

    if check_str == len(check_str) * check_str[0] and check_str[0] == 0:
        # all are the same and zero, just strip it
        check_str = ''

    lit_list_comb = ''.join(lit_list)
    rtn_int = int(lit_list_comb, 2)

    return rtn_str, rtn_int


def hex_to_bin(hex_str):
    rtn_str = ''
    conc_list = []
    for c in hex_str:
        temp_str = str(bin(int(c, 16)))[2:].zfill(4)
        conc_list.append(temp_str)

    rtn_str = ''.join(conc_list)
    return rtn_str


def data_import():
    #day16_data_file = open('day16data.txt', 'r')
    day16_data_file = open('day16data_ut.txt', 'r')

    day16_data_list = day16_data_file.read().splitlines()

    return day16_data_list


if __name__ == "__main__":
    print('__name__')
    main()

