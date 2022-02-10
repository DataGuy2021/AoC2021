import numpy as np


def main():
    start_list = data_import()
    array_axis_1 = len(start_list[0])
    array_axis_0 = len(start_list)
    np_temp_arr = np.ndarray(shape=(array_axis_0, array_axis_1), dtype=int)  # 0/Y(up/down) 1/X(L/R)

    for i, d in enumerate(start_list):
        # print(f"{i}:{d}")
        np_temp_arr[i] = list(d)
    print(np_temp_arr)

    risk_level_list = []

    # check all index
    it = np.nditer(np_temp_arr, flags=['multi_index'])
    for z in it:
        # print(f"{z}:{it.multi_index}")
        # print(type(it.multi_index))  # (row, column)
        axis_1_x = it.multi_index[1]
        axis_0_y= it.multi_index[0]

        if axis_1_x == array_axis_1 - 1:
            x_plus = -1
        else:
            x_plus = axis_1_x + 1

        if axis_1_x == 0:
            x_minus = -1
        else:
            x_minus = axis_1_x - 1

        if axis_0_y == array_axis_0 - 1:
            y_plus = -1
        else:
            y_plus = axis_0_y + 1

        if axis_0_y == 0:
            y_minus = -1
        else:
            y_minus = axis_0_y - 1

        if x_plus != -1:
            if z < np_temp_arr[axis_0_y, x_plus]:  # [row, column]
                x_plus_bool = True
            else:
                x_plus_bool = False
        else:
            x_plus_bool = True

        if x_minus != -1:
            if z < np_temp_arr[axis_0_y, x_minus]:
                x_minus_bool = True
            else:
                x_minus_bool = False
        else:
            x_minus_bool = True

        if y_plus != -1:
            if z < np_temp_arr[y_plus, axis_1_x]:
                y_plus_bool = True
            else:
                y_plus_bool = False
        else:
            y_plus_bool = True

        if y_minus != -1:
            if z < np_temp_arr[y_minus, axis_1_x]:
                y_minus_bool = True
            else:
                y_minus_bool = False
        else:
            y_minus_bool = True

        if x_plus_bool and x_minus_bool and y_plus_bool and y_minus_bool:
            risk_level_list.append(z + 1)
            #print(f'xm:{x_minus},ym:{y_minus},xp:{x_minus},yp:{y_plus}')
            #print(f'{axis_0_y}, {axis_1_x}')

    print(risk_level_list)
    print(sum(risk_level_list))


def data_import():
    #day9_data_file = open('day9data.txt', 'r')
    day9_data_file = open('day9data_ut.txt', 'r')

    day9_data_list = day9_data_file.read().splitlines()

    return day9_data_list


if __name__ == "__main__":
    main()
